pipeline {
   agent { docker { image 'mcr.microsoft.com/playwright/python:v1.49.1-noble' } }
   stages {
      stage('e2e-tests') {
         steps {
            sh 'pip install -r requirements.txt'
            sh 'pytest'
         }
      }
   }
}