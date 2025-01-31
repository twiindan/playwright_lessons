pipeline {
   agent { docker { image 'python' } }
   stages {
      stage('Install dependencies') {
         steps {
            sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
         }
      }
   }
}