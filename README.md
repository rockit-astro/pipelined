## Data pipeline daemon

Part of the observatory software for the Warwick La Palma telescopes.

`pipelined` manages the data pipeline for frames after they have been acquired:

* Adding telescope and environment header cards
* Archiving frames to disk
* Extracting frame properties for opsd (e.g. x/y profiles for autoguiding, HFDs for focusing, median intensity for flats)
* Generating previews for the web dashboard

`pipeline` is a commandline utility for configuring the pipeline.

See [Software Infrastructure](https://github.com/warwick-one-metre/docs/wiki/Software-Infrastructure) for an overview of the W1m software architecture and instructions for developing and deploying the code.

### Software setup

After installing `<telescope>-pipeline-server`, the `pipelined` must be enabled using:
```
sudo systemctl enable pipelined@<telescope>
```

The service will automatically start on system boot, or you can start it immediately using:
```
sudo systemctl start pipelined@<telescope>
```

Next, open a port in the firewall so that other machines on the network can access the daemon:
```
sudo firewall-cmd --zone=public --add-port=<port>/tcp --permanent
sudo firewall-cmd --reload
```
where <port> is (defined in the warwick-observatory-common daemon config).

Finally, we need to set up NFS to mount the gotoserver dashboard generated directory so that we can write live data previews.
Edit `/etc/fstab` and add
```
10.2.6.100:/srv/dashboard/generated /mnt/dashboard-generated/   nfs defaults 0 0
```
then reboot.

If you want to run ds9 previews from *another* machine (e.g. onemetre-dome) then you will need to open up the firewall on that machine to accept connections from `pipelined`.  The simplest way to allow this, for now, is to whitelist all ports using:
```
firewall-cmd --zone=public --add-rich-rule='rule family="ipv4" source address="<pipelined host ip>" accept' --permanent
```

The configuration (including things like header cards, ds9 preview properties) is defined in the json file for each telescope.
