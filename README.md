## Data pipeline daemon

`pipelined` manages the data pipeline for frames after they have been acquired:

* Adding telescope and environment header cards
* Archiving frames to disk
* Extracting frame properties for opsd (e.g. x/y profiles for autoguiding, HFDs for focusing, median intensity for flats)
* Generating previews for the web dashboard

The actual processing is done by `pipeline_workerd`, which runs as a separate daemon for each camera (possibly on separate machines).

`pipeline` is a commandline utility for configuring the pipeline.

### Configuration

Configuration is read from json files that are installed by default to `/etc/pipelined`.
A configuration file is specified when launching the server, and the `pipeline` frontend will search this location when launched.

The configuration options are:
```python
{
  "daemon": "localhost_test2", # Run the server as this daemon. Daemon types are registered in `rockit.common.daemons`.
  "log_name": "pipelined@test", # The name to use when writing messages to the observatory log.
  "control_machines": ["LocalHost"],  # Machine names that are allowed to control (rather than just query) state. Machine names are registered in `rockit.common.IP`.
  "notify_frame_machines": ["LocalHost"], # Machine names that are running camera daemons that should be processed by this server.
  "environment_daemon": "localhost_test4", # The daemon that should be queried to fetch environment data. See environmentd project.
  "environment_query_timeout": 1, # The maximum timeout when querying environment data. Frame headers will be marked as not available if this expires.
  "telescope_query_timeout": 1, # The maximum timeout when querying telescope data. Frame headers will be marked as not available if this expires.
  "ops_daemon": "localhost_test5", # The operations daemon that should be notified when a frame is processed. See opsd project.
  "guiding_min_interval": 5, # The minimum interval (in seconds) between autoguider update calculations.
  "cameras": {
    "TEST": {
      "worker_daemon": "localhost_test3", # Run the worker service as this daemon. Daemon types are registered in `rockit.common.daemons`.
      "worker_processes": 2, # Number of worker processes that a spawned to process frames in parallel
      "input_data_path": "/data/incoming", # The directory where camera daemons save frames before calling notify_frame.
      "output_data_path": "/data",  # The root path under which nightly data directories are created.
      "ccd_bin_card": "CCD-XBIN", # (optional) Header card (from the camera daemon) to multiply with platescale.
      "image_region_card": "IMAG-RGN", # (optional) Header card (from the camera daemon) to crop frame before source detection or intensity statistics.
      "overscan_region_card": "BIAS-RGN", # (optional) Header card (from the camera daemon) to measure overscan bias level to subtract from intensity statistics.
      "platescale": 0.391, # Image platescale used to convert px HFDs to arcsec.
      "object_minpix": 16, # Minimum object pixel count for source detection.
      "preview_min_interval": 5,# The minimum interval (in seconds) between preview updates.
      "preview_max_instances": 5, # Maximum number of ds9 previews that can be active for this camera 
      "preview_ds9_width": 512, # Default ds9 window width for pipeline preview windows.
      "preview_ds9_height": 572, # Default ds9 window height for pipeline preview windows.
      "preview_ds9_zoom": 0.5, # Default ds9 window zoom for pipeline preview windows.
      "preview_ds9_annotation_margin": 30, # Pixel offset for information annotations above/below the ds9 preview.
      "hfd_grid_tiles_x": 5, # Number of vertical slices used by the hfd grid previews
      "hfd_grid_tiles_y": 4, # Number of horizontal slices used by the hfd grid previews
      "wcs": {
        "scale_low": 0.38, # Scale parameter for astrometry.net; arcsec per px.
        "scale_high": 0.40, # Scale parameter for astrometry.net; arcsec per px.
        "timeout": 4.0, # Solution timeout for astrometry.net.
        "tel_ra_card": "TELRA", # (optional) Header card (from telescope_cards below) with the estimated telescope RA.
        "tel_dec_card": "TELDEC", # (optional) Header card (from telescope_cards below) with the estimated telescope Dec.
        "search_radius": 1.75, # (optional) Maximum search radius (in degrees) around the search ra/dec.   
      },
      "dashboard": {
          "user": "ops", # User on the local machine that owns the SSH key for copying files to the dashboard
          "key": "dashboard", # SSH key file to use for copying files to the dashboard
          "remote_host": "GOTOServer", # Dashboard host machine
          "remote_user": "dashboarddata", # User on the dashboard host to log in as
          "remote_path": "/srv/dashboard/generated", # Directory on the dashboard host to copy files to
          "prefix": "dashboard-CAM1", # The filename prefix to use for generated preview data.
          "flip_vertical": true, # Flip dashboard preview image vertically.
          "flip_horizontal": false, # Flip dashboard preview image horizontally.
          "min_threshold": 5, # Histogram black level (in percent) for dashboard previews.
          "max_threshold": 95, # Histogram white level (in percent) for dashboard previews.
          "thumb_size": 1024, # Dashboard thumbnail size.
          "clip_size": 1024, # Clip a region this big around the center of the image for the dashboard zoom preview.
          "min_interval": 30, # The minimum interval (in seconds) between dashboard updates.
      }
    }
    # Additional cameras can be defined.
  },
  "environment_cards": [ # Header cards to add under the ENVIRONMENT section.
    {
      "key": "EXTTEMP", # Header keyword
      "comment": "[deg c] temperature outside dome", # Header comment.
      "sensor": "w1m_vaisala", # sensor in the environmentd data dictionary.
      "parameter": "temperature", # parameter under the sensor block in the environmentd data dictionary.
      "type": "float1dp" # Format type (float1dp, float2dp, float5dp, int, string, bool).
    }
    # Additional header cards can be defined.
  ],
  "telescope_cards": [ # Header cards to add under the TELESCOPE section.
    {
      "key": "TELSWVER", # Header keyword.
      "comment": "tcs server software version", # Header comment.
      "type": "string", # Format type (float1dp, float2dp, float5dp, int, string, bool).
      "daemon": "localhost_test3", # The daemon that should be queried. It must define a report_status method.
      "parameter": "software_version" # The parameter in the report_status data.
    }
    # Additional header cards can be defined.
  ]
}
```


### Initial Installation


The automated packaging scripts will push 6 RPM packages to the observatory package repository:

| Package                        | Description                                                                       |
|--------------------------------|-----------------------------------------------------------------------------------|
| rockit-pipeline-server         | Contains the `pipelined` and `pipeline_workerd` servers and systemd service file. |
| rockit-pipeline-client         | Contains the `pipeline` commandline utility for controlling the pipeline server.  |
| rockit-pipeline-data-clasp     | Contains the json configuration for the CLASP pipeline installation.              |
| rockit-pipeline-data-halfmetre | Contains the json configuration for the Half metre pipeline installation.         |
| rockit-pipeline-data-onemetre  | Contains the json configuration for the W1m pipeline installation.                |
| rockit-pipeline-data-superwasp | Contains the json configuration for the SuperWASP pipeline installation.          |
| python3-rockit-pipeline        | Contains the python module with shared code.                                      |

After installing packages, the main systemd service should be enabled:

```
sudo systemctl enable --now pipelined@<telescope>
```

where `telescope` is the name of the json file for the appropriate telescope.

Enable the systemd services for each camera worker:

```
sudo systemctl enable --now pipeline_workerd@<telescope_camera>
```

where `telescope` is the name of the json file for the appropriate telescope and camera is the camera ID.
These map to an .args file in `/etc/pipelined`.

Now open a port in the firewall:
```
sudo firewall-cmd --zone=public --add-port=<port>/tcp --permanent
sudo firewall-cmd --reload
```
where `port` is the port defined in `rockit.common.daemons` for the daemon specified in the pipeline config.

If you want to run ds9 previews from *another* machine (e.g. `onemetre-dome`) then you will need to make sure that the machine running the server can connect to the client machine over ssh (to establish a tunnel) without requiring manual input. Set up login keys and host config as needed.

### Upgrading Installation

New RPM packages are automatically created and pushed to the package repository for each push to the `master` branch.
These can be upgraded locally using the standard system update procedure:
```
sudo yum clean expire-cache
sudo yum update
```

The daemon should then be restarted to use the newly installed code:
```
sudo systemctl restart pipelined@<config>
```

### Testing Locally

The pipeline server and client can be run directly from a git clone:
```
./pipelined config/test.json
PIPELINED_CONFIG_PATH=./config/test.json ./pipeline status
```
