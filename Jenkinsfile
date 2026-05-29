pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "sumanji73/skc-chatbot-api"
        IMAGE_TAG = "latest"
    }

    stages {
        stage('Clone Code') {
            steps {
                git branch: 'main',
                url: 'https://github.com/sumanji/deployment-Test.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Changed from sh to bat, and updated variable syntax to %VAR%
                bat "docker build -t %DOCKER_IMAGE%:%IMAGE_TAG% ."
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    // Changed to bat and wrapped the multiline block in double quotes
                    bat """
                    echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin
                    docker push %DOCKER_IMAGE%:%IMAGE_TAG%
                    docker logout
                    """
                }
            }
        }
    }
}
