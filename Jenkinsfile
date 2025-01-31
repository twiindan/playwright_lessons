pipeline {
   agent any
   stages {
      stage('Install dependencies') {
         steps {
            sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip3 install -r requirements.txt
                '''
         }
      }
      stage('Execute tests') {
         steps {
            sh '''
                pytest playwright/test_playwright_fixtures.py
                '''
         }
      }
   }
}