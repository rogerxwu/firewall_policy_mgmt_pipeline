pipeline {
    agent { dockerfile true }
    stages {
        stage('Test') {
            steps {
                sh 'python3 -V'
                sh 'cd firewall_policy_mgmt_pipeline'
                sh 'python3 deploy_to_network.py'
            }
        }
    }
}