pipeline {
   agent { docker { image 'mcr.microsoft.com/playwright/python:v1.49.1-noble' } }
   stages {
      stage('Install dependencies') {
         steps {
             sh 'apt install python3.12-venv'
             sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
         }
      }
   }
}