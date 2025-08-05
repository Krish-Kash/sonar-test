pipeline {
    agent any

    environment {
        // Define environment variables if needed
        APP_NAME = 'SampleApp'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building the application...'
                // Replace with actual build command
                // sh './build.sh'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // Replace with actual test command
                // sh './run-tests.sh'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                // Replace with actual deploy command
                // sh './deploy.sh'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}


