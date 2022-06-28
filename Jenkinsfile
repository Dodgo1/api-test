pipeline{
    agent{
        label 'jenkins-node-intern'
    }
    stages{
        stage("setup docker agent"){
            agent {
                docker {
                    label 'jenkins-node-intern'
                    image 'python:3.10-alpine'
                    args '-u root:root'
                }
            }
            stages{
                stage("install dependencies"){
                    steps{
                        sh """
                        pip install pipenv
                        pipenv install
                        """
                    }
                }
                stage("run tests"){
                     environment {
                        API_KEY = "59e62469a3da06b2a9a30ff73c2c0d05"
                     }
                    steps{
                        sh """
                        pipenv run pytest test_main.py
                        """
                    }
                }
            }
        }
    }
}