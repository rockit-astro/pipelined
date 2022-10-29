## Data pipeline daemon

`pipelined` manages the data pipeline for frames after they have been acquired:

* Adding telescope and environment header cards
* Archiving frames to disk
* Extracting frame properties for opsd (e.g. x/y profiles for autoguiding, HFDs for focusing, median intensity for flats)
* Generating previews for the web dashboard

The actual processing is done by `pipeline_workerd`, which runs as a separate daemon for each camera (possibly on separate machines).

`pipeline` is a commandline utility for configuring the pipeline.

See [Software Infrastructure](https://github.com/warwick-one-metre/docs/wiki/Software-Infrastructure) for an overview of the observatory software architecture and instructions for developing and deploying the code.

### Configuration

Configuration is read from json files that are installed by default to `/etc/pipelined`.
A configuration file is specified when launching the server, and the `pipeline` frontend will search this location when launched.

The configuration options are:
```python
{
  "daemon": "localhost_test2", # Run the server as this daemon. Daemon types are registered in `warwick.observatory.common.daemons`.
  "log_name": "pipelined@test", # The name to use when writing messages to the observatory log.
  "control_machines": ["LocalHost"],  # Machine names that are allowed to control (rather than just query) state. Machine names are registered in `warwick.observatory.common.IP`.
  "notify_frame_machines": ["LocalHost"], # Machine names that are running camera daemons that should be processed by this server.
  "environment_daemon": "localhost_test4", # The daemon that should be queried to fetch environment data. See environmentd project.
  "environment_query_timeout": 1, # The maximum timeout when querying environment data. Frame headers will be marked as not available if this expires.
  "telescope_query_timeout": 1, # The maximum timeout when querying telescope data. Frame headers will be marked as not available if this expires.
  "ops_daemon": "localhost_test5", # The operations daemon that should be notified when a frame is processed. See opsd project.
  "guiding_min_interval": 5, # The minimum interval (in seconds) between autoguider update calculations.
  "cameras": {
    "TEST": {
      "worker_daemon": "localhost_test3", # Run the worker service as this daemon. Daemon types are registered in `warwick.observatory.common.daemons`.
      "worker_processes": 2, # Number of worker processes that a spawned to process frames in parallel
      "input_data_path": "/data/incoming", # The directory where camera daemons save frames before calling notify_frame.
      "output_data_path": "/data",  # The root path under which nightly data directories are created.
      "dashboard_user": "ops",
      "dashboard_key": "dashboard",
      "dashboard_remote_user": "dashboarddata",
      "dashboard_remote_host": "GOTOServer",
      "dashboard_remote_path": "/srv/dashboard/generated",
      "dashboard_prefix": "dashboard-CAM1", # The filename prefix to use for generated preview data.
      "wcs_scale_low": 0.38, # Scale parameter for astrometry.net; arcsec per px.
      "wcs_scale_high": 0.40, # Scale parameter for astrometry.net; arcsec per px.
      "wcs_timeout": 4.0, # Solution timeout for astrometry.net.
      "wcs_search_ra_card": "TELRA", # (optional) Header card (from telescope_cards below) with the estimated telescope RA.
      "wcs_search_dec_card": "TELDEC", # (optional) Header card (from telescope_cards below) with the estimated telescope Dec.
      "wcs_search_radius": 1.75, # (optional) Maximum search radius (in degrees) around the search ra/dec.
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
      "dashboard_flip_vertical": true, # Flip dashboard preview image vertically.
      "dashboard_flip_horizontal": false, # Flip dashboard preview image horizontally.
      "dashboard_min_threshold": 5, # Histogram black level (in percent) for dashboard previews.
      "dashboard_max_threshold": 95, # Histogram white level (in percent) for dashboard previews.
      "dashboard_thumb_size": 1024, # Dashboard thumbnail size.
      "dashboard_clip_size": 1024, # Clip a region this big around the center of the image for the dashboard zoom preview.
      "dashboard_min_interval": 30, # The minimum interval (in seconds) between dashboard updates.
      "hfd_grid_tiles_x": 5, # Number of vertical slices used by the hfd grid previews
      "hfd_grid_tiles_y": 4 # Number of horizontal slices used by the hfd grid previews
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

| Package           | Description |
| ----------------- | ------ |
| observatory-pipeline-server | Contains the `pipelined` and `pipeline_workerd` servers and systemd service file. |
| observatory-pipeline-client | Contains the `pipeline` commandline utility for controlling the pipeline server. |
| python3-warwick-observatory-pipeline | Contains the python module with shared code. |
| onemetre-pipeline-data | Contains the json configuration for the W1m pipeline installation. |
| clasp-pipeline-data | Contains the json configuration for the CLASP pipeline installation. |
| superwasp-pipeline-data | Contains the json configuration for the SuperWASP pipeline installation. |

The `observatory-pipeline-server` and `observatory-pipeline-client` and `onemetre-pipeline-data` packages should be installed on the `onemetre-tcs` TCS machine.

The `observatory-pipeline-server` and `observatory-pipeline-client` and `clasp-pipeline-data` packages should be installed on the `clasp-tcs` TCS machine.

The `observatory-pipeline-server` and `observatory-pipeline-client` and `superwasp-pipeline-data` packages should be installed on the `superwasp-tcs` TCS machine.

After installing packages, the main systemd service should be enabled:

```
sudo systemctl enable pipelined@<telescope>
sudo systemctl start pipelined@<telescope>
```

where `telescope` is the name of the json file for the appropriate telescope.

Enable the systemd services for each camera worker:

```
sudo systemctl enable pipeline_workerd@<telescope_camera>
sudo systemctl start pipeline_workerd@<telescope_camera>
```

where `telescope` is the name of the json file for the appropriate telescope and camera is the camera ID.
These map to an .args file in `/etc/pipelined`.

Now open a port in the firewall:
```
sudo firewall-cmd --zone=public --add-port=<port>/tcp --permanent
sudo firewall-cmd --reload
```
where `port` is the port defined in `warwick.observatory.common.daemons` for the daemon specified in the pipeline config.

Finally, we need to set up NFS to mount the gotoserver dashboard generated directory so that we can write live data previews.
Edit `/etc/fstab` and add
```
10.2.6.100:/srv/dashboard/generated /mnt/dashboard-generated/   nfs defaults 0 0
```
then reboot.

If you want to run ds9 previews from *another* machine (e.g. `onemetre-dome`) then you will need to make sure that the machine running the server can connect to the client machine over ssh (to establish a tunnel) without requiring manual input. Set up login keys and host config as needed.

The SuperWASP TCS should export a data partition for the camera pis to write to.

Edit `/etc/exports` and add:

```
/data/wasp   10.2.6.120(rw,sync,no_root_squash,no_all_squash) 10.2.6.121(rw,sync,no_root_squash,no_all_squash)
```

Next enable the NFS daemons:
```
sudo systemctl enable rpcbind
sudo systemctl enable nfs-server
sudo firewall-cmd --permanent --zone=public --add-service=nfs
sudo firewall-cmd --permanent --zone=public --add-service=mountd
sudo firewall-cmd --permanent --zone=public --add-service=rpc-bind
sudo firewall-cmd --reload
```

and `systemctl start` them or reboot.

### Upgrading Installation

New RPM packages are automatically created and pushed to the package repository for each push to the `master` branch.
These can be upgraded locally using the standard system update procedure:
```
sudo yum clean expire-cache
sudo yum update
```

The daemon should then be restarted to use the newly installed code:
```
sudo systemctl stop pipelined@<config>
sudo systemctl start pipelined@<config>
```

### Testing Locally

The pipeline server and client can be run directly from a git clone:
```
./pipelined test.json
PIPELINED_CONFIG_PATH=./test.json ./pipeline status
```
