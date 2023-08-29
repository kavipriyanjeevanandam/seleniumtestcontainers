pipeline {
  agent any
  stages {
    stage('Checkout') {
            steps {
                // Checkout code from version control
                checkout scm
            }
        }
    stage('Build testing env') {
            steps {
                bat "docker build -t seleniumenvv:0.1 ."
                    
            }
        }

    stage('Test') {
      steps{
      bat "docker run -d -p 5000:5000 --network ml_network --name backend kavipriyanjeevanandam/ml-flask:0.1"
      bat "docker run -d -p 80:80 --network ml_network --name frontendcontainer kavipriyanjeevanandam/ml-angular:0.1"
      bat "docker run --name selenium --network ml_network seleniumenvv:0.1"
      }
    }
  }
  post {
        always {
            // Stop and remove all containers
            bat "docker stop frontendcontainer"
            bat "docker stop backend"
            bat "docker rm frontendcontainer"
            bat "docker rm backend"
            bat "docker rm selenium"
        }
    }


}
