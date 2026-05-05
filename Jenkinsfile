pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/nare-shh/flask-k8s-app.git'
            }
        }
        stage('Build Image') {
            steps {
                sh 'docker build -f Dockerfile.healthcare -t healthcare-app:latest . || docker build -t healthcare-app:latest .'
            }
        }
        stage('Stop Old') {
            steps {
                sh 'docker stop healthcare-app || true'
                sh 'docker rm healthcare-app || true'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker run -d --name healthcare-app -p 5000:5000 healthcare-app:latest'
            }
        }
        stage('Verify') {
            steps {
                sh 'docker ps | grep healthcare'
                sh 'curl -s http://localhost:5000/health'
            }
        }
    }
    post {
        success { echo 'Healthcare app deployed successfully!' }
        failure { echo 'Deployment failed. Check logs.' }
    }
}
