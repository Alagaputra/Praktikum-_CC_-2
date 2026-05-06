pipeline {
    agent any

    environment {
        DOCKER_HUB = 'whosg'
        FRONTEND_IMAGE = "${DOCKER_HUB}/praktikum-frontend"
        BACKEND_IMAGE = "${DOCKER_HUB}/praktikum-backend"
        IMAGE_TAG = "latest"
    }

    stages {
        stage('Checkout') {
            steps {
                // Mengambil kode terbaru dari repositori GitHub
                checkout scm
            }
        }

        stage('Build & Push') {
            steps {
                script {
                    // Login ke Docker Hub
                    withCredentials([usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )]) {
                        bat "docker login -u %DOCKER_USER% -p %DOCKER_PASS%"

                        // Build dan push backend image
                        bat "docker build -t %BACKEND_IMAGE%:%IMAGE_TAG% ./backend"
                        bat "docker push %BACKEND_IMAGE%:%IMAGE_TAG%"

                        // Build dan push frontend image
                        bat "docker build -t %FRONTEND_IMAGE%:%IMAGE_TAG% ./frontend"
                        bat "docker push %FRONTEND_IMAGE%:%IMAGE_TAG%"
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Deploy ke AKS menggunakan kubeconfig
                    withCredentials([file(
                        credentialsId: 'kubeconfig-credential',
                        variable: 'KUBECONFIG'
                    )]) {
                        bat "kubectl apply -f k8s/backend-deployment.yaml --kubeconfig=%KUBECONFIG%"
                        bat "kubectl apply -f k8s/backend-service.yaml --kubeconfig=%KUBECONFIG%"
                        bat "kubectl apply -f k8s/frontend-deployment.yaml --kubeconfig=%KUBECONFIG%"
                        bat "kubectl apply -f k8s/frontend-service.yaml --kubeconfig=%KUBECONFIG%"
                        bat "kubectl apply -f k8s/ingress.yaml --kubeconfig=%KUBECONFIG%"
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment berhasil!'
        }
        failure {
            echo 'Deployment gagal. Periksa log untuk detail.'
        }
    }
}
