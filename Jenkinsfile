pipeline {
    agent any

    options {
        skipDefaultCheckout()
    }

    stages {
        stage('Environment Check') {
            steps {
                echo 'Перевірка інтерпретатора Python...'
                bat '''
                    chcp 65001
                    powershell -NoProfile -ExecutionPolicy Bypass -Command "Write-Host 'Active Python interpreter:'; & 'D:\\університет\\3\\tp\\lab2_testing\\venv\\Scripts\\python.exe' --version"
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