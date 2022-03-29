pipeline {
     agent none
     stages {
         stage('build') {
            steps {
                // One or more steps need to be included within the steps block.
                agent {
                    docker {
                        image 'python:3.8-alpine'
                    }
                }
            }
        }
        stages {
            sh 'pip install -r requirements.txt'
            sh 'python /usr/src/app/Flask.py'
        }
    }
}