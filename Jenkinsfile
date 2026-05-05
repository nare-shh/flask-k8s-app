pipeline {
    agent any

    environment {
        DOCKERHUB_CREDS = credentials('dockerhub-cred')
        DOCKERHUB_USER  = 'nareshhh'
        IMAGE_NAME      = "${DOCKERHUB_USER}/flask-app"
        IMAGE_TAG       = "${BUILD_NUMBER}"
    }

    stages {
        stage('1 - Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/nare-shh/flask-k8s-app.git'
                echo "Code cloned successfully"
            }
        }

        stage('2 - Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
                sh "docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${IMAGE_NAME}:latest"
                echo "Docker image built"
            }
        }

        stage('3 - Push to DockerHub') {
            steps {
                sh """
                    echo ${DOCKERHUB_CREDS_PSW} | docker login -u ${DOCKERHUB_CREDS_USR} --password-stdin
                    docker push ${IMAGE_NAME}:${IMAGE_TAG}
                    docker push ${IMAGE_NAME}:latest
                """
                echo "Image pushed to DockerHub"
            }
        }

        stage('4 - Deploy to Kubernetes') {
            steps {
                sh """
                    sed -i 's|YOURDOCKERHUBUSERNAME/flask-app:latest|${IMAGE_NAME}:${IMAGE_TAG}|g' k8s/deployment.yaml
                    kubectl apply -f k8s/deployment.yaml
                    kubectl rollout status deployment/flask-app --timeout=120s
                """
                echo "Deployed to Kubernetes"
            }
        }

        stage('5 - Verify') {
            steps {
                sh "kubectl get pods -l app=flask-app"
                sh "kubectl get svc flask-service"
            }
        }
    }

    post {
        success {
            echo "SUCCESS! Pipeline completed"
        }
        failure {
            echo "FAILED. Check logs above"
        }
        always {
            sh "docker logout"
            sh "docker rmi ${IMAGE_NAME}:${IMAGE_TAG} || true"
        }
    }
}
