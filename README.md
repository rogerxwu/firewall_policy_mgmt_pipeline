# Firewall Policy Management Pipeline

## Workflow

Change merged to github -> Trigger Jenkins build job -> Prepare the docker container -> Render firewall policy configuration -> Validate the change -> Push to the device

## Pre-reqirement
1. Github
    webhook configured to delievery evnent to Jenkins instance when change is merged to 'prod' branch
2. Jenkins
3. Jenkins Job
    Set souce code management to Github project repo
    CHecked GitHub hook trigger for GITScm polling
3. firewall instance running on virtual env

## Each Components Setup
### Github Setup
Setup webhook to trigger the Jenkins build job when merge event occured

### vSRX Setup
vSRX instance account [root/1qaz2wsx] 
vSRX junos account [admin/123]
1. Download vSRX image from https://webdownload.juniper.net/swdl/dl/download
2. Run vSRX in VMware Fusion
    1. Setup Network Adapter to 'Private to my mac'
    2. Setup fxp0.0 to the same subnet IP for Network Adapter
    ```
    set interfaces fxp0 unit 0 family inet address [IP/Netmask]
    ```
    3. Add the following config
    ```
    set system services ssh
    set system services netconf ssh
    ```
3. Test the connection using naplam

### Jenkins Setup
Jenkins account [admin/123]
1. Create Dockerfile to define the environment running the script
2. Create Jenkinsfile to define the pipeline work


## Reference
1. Automating ACLs with Aerleon and Pandas https://vimeo.com/830550340/3c558ad696
2. Napalm https://napalm.readthedocs.io/en/latest/tutorials/samples.html
3. Juniper Software download https://webdownload.juniper.net/swdl/dl/download