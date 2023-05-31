pipeline {
    agent {
        dockerContainer { image 'alpine:3.17' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'python3 -V'
            }
        }
    }
}