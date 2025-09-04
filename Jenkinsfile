pipeline {
    agent any

    environment {
        // Define environment variables
        APP_NAME = 'MyApp'
        BUILD_ENV = 'dev'
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
                echo "Building ${APP_NAME} in ${BUILD_ENV} environment..."
                // Example build command
                sh './gradlew build'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // Example test command
                sh './gradlew test'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                // Example deploy command
                sh './deploy.sh'
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


