pipeline {
    agent any
    
    stages {
        stage('Fetch Code') {
            steps {
                git https://github.com/Krish-Kash/sonar-test.git
            }
        }
        stage('Code Analysis') {
            environment {
                scannerHome = tool 'Sonar'
            }
            steps {
                script {
                    withSonarQubeEnv('Sonar') {
                        sh "${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=kkash6-test-project \
                            -Dsonar.projectName=kkash6-test-project \
                            -Dsonar.projectVersion=1.0 \
                            -Dsonar.sources=."
                    }
                }
            }
        }
    }
}


