pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Test & XML Report') {
            steps {
                // Встановлюємо плагін для генерації XML-звітів (Вимога 1)
                sh 'pip install unittest-xml-reporting'
                
                // Запускаємо твої тести через xmlrunner. Він створить папку test-reports з XML
                sh 'python -m xmlrunner test_salon_manager.py -o test-reports'
            }
            post {
                always {
                    // Вказуємо Jenkins, де шукати згенерований XML для побудови графіків
                    junit 'test-reports/*.xml'
                }
            }
        }
        
        stage('Build Docker Image') {
            steps {
                // Збираємо образ твого додатку (Вимога 2)
                sh 'docker build -t KaterynaCherneha/lab2_testing:v1.0 .'
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                // Завантажуємо образ на Docker Hub (Вимога 2)
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                    sh 'echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin'
                    sh 'docker push KaterynaCherneha/lab2_testing:v1.0'
                }
            }
        }
    }
}