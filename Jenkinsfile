pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Отримання вихідного коду проєкту...'
            }
        }

        stage('Environment Check') {
            steps {
                bat '''
                    chcp 65001
                    powershell -NoProfile -ExecutionPolicy Bypass -Command "Write-Host 'Active Python interpreter:'; & '.\\venv\\Scripts\\python.exe' --version"
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Запуск модульних тестів салону краси...'
                bat '''
                    chcp 65001
                    powershell -NoProfile -ExecutionPolicy Bypass -Command "Set-Location 'D:\\університет\\3\\tp\\lab2_testing'; & '.\\venv\\Scripts\\python.exe' -m unittest test_salon_manager.py"
                '''
            }
        }
    }

    post {
        always {
            echo 'Пайплайн завершив роботу.'
        }
        success {
            echo 'Всі етапи збірки та тести пройшли успішно!'
        }
        failure {
            echo 'Сталася помилка під час виконання збірки.'
        }
    }
}