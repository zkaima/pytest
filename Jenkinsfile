pipeline {
     agent none
     stages {
         stage('build') {
            steps {
                // One or more steps need to be included within the steps block.
                agent {
                    docker {
                        image 'python:3-alpine'
                    }
                }
            }
        }
        stages {
            sh 'pip install -r requirements.txt'
            sh 'python Flask.py'
        }
    }
}