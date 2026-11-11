pipeline {
    agent any
    options {
        skipDefaultCheckout()
    }
    stages {
        stage('Test & Generate XML') {
            steps {
                echo 'Запуск тестів та генерація XML звіту...'
                bat '''
                chcp 65001
                powershell -NoProfile -ExecutionPolicy Bypass -Command "Set-Location 'D:\\університет\\3\\tp\\lab2_testing'; & '.\\venv\\Scripts\\pip.exe' install unittest-xml-reporting; & '.\\venv\\Scripts\\python.exe' -m xmlrunner test_salon_manager.py -o test-reports"
                '''
            }
            post {
                always {
                    // Пункт 1: Jenkins зчитує XML для графіка
                    junit 'test-reports/*.xml'
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                echo 'Створення Docker образу...'
                // Пункт 2: Створення образу
                bat '''
                chcp 65001
                powershell -NoProfile -ExecutionPolicy Bypass -Command "Set-Location 'D:\\університет\\3\\tp\\lab2_testing'; docker build -t katerynacherneha/salon-manager:latest ."
                '''
            }
        }
        stage('Push to Docker Hub') {
            steps {
                echo 'Відправка образу на Docker Hub...'
                // Пункт 2: Авторизація та відправка образу
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                    bat 'echo %DOCKER_PASS%| docker login -u %DOCKER_USER% --password-stdin'
                    bat 'docker push katerynacherneha/salon-manager:latest'
                }
            }
        }
    }
}