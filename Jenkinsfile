pipeline {
   agent { docker { image 'python' } }
   stages {
      stage('Install dependencies') {
         steps {
            sh '''
                pip install -r requirements.txt
                '''
         }
      }
   }
}