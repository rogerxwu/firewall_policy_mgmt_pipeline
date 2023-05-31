# Firewall Policy Management Pipeline

## Workflow

Change merged to github -> Trigger Jenkins build job -> Render firewall policy configuration -> Validate the change -> Push to the device

## Pre-reqirement
1. Github
    webhook configured to delievery evnent to Jenkins instance when change is merged to 'prod' branch
2. Jenkins
3. Jenkins Job
    Set souce code management to Github project repo
    CHecked GitHub hook trigger for GITScm polling
3. firewall instance running on virtual env


Manually trigger Jenkins build job
Render firewall policy configuration on MacOS
Pre-defined a docker image
Render firewall policy configuration from docker image

vSRX instance account [root/1qaz2wsx] 
vSRX junos account [admin/123]

## Reference
1. Automating ACLs with Aerleon and Pandas https://vimeo.com/830550340/3c558ad696
2. Napalm https://napalm.readthedocs.io/en/latest/tutorials/samples.html
3. Juniper Software download https://webdownload.juniper.net/swdl/dl/download