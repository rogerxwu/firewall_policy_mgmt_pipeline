pipeline {
    agent {
        docker { image 'alpine:3.17' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'python3 -V'
            }
        }
    }
}