pipeline {
    agent any

    environment {
        // Replace with your actual SonarQube server name configured in Jenkins
        SONARQUBE_SERVER = 'SonarQube Server'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from GitHub
                git url: 'https://github.com/Krish-Kash/sonar-test.git', branch: 'main'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    // Run SonarQube scanner for Python project
                    def scannerHome = tool 'SonarQubeScanner'
                    withSonarQubeEnv("${SONARQUBE_SERVER}") {
                        sh "${scannerHome}/bin/sonar-scanner                             -Dsonar.projectKey=sonar-test-project                            -Dsonar.sources=.                             -Dsonar.language=py                             -Dsonar.python.version=3.8                             -Dsonar.sourceEncoding=UTF-8"
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 1, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
        success {
            echo 'SonarQube analysis passed.'
        }
        failure {
            echo 'SonarQube analysis failed or quality gate not passed.'
        }
    }
}

