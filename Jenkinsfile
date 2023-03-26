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
                        API_KEY = *SECRET*
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