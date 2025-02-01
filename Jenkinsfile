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
                SELENIUM_REMOTE_URL=http://127.0.0.1:4444 python3 -m pytest framework/test_with_faker.py --alluredir allure-results
                '''
         }
         post {
                always {
                    allure includeProperties:
                     false,
                     jdk: '',
                     results: [[path: 'allure-results']]
                }
         }
      }
   }
}