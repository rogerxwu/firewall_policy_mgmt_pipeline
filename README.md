# Firewall Policy Management Pipeline

## Workflow

Change merged to github -> Trigger Jenkins build job -> Render firewall policy configuration -> Validate the change -> Push to the device

## Pre-reqirement
1. Github
2. Jenkins
3. firewall instance running on virtual env






## How to trigger the pipeline build from github to Jenkins
1. Install Jenkins by following https://www.jenkins.io/download/lts/macos/

2. Create a Jenkins build job that uses a GitHub URL
