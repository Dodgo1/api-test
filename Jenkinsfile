pipeline{
    agent{
        label 'jenkins-node-intern'
    }
    stages{
        stage("run a test"){
            agent {
                docker {
                    label 'jenkins-node-intern'
                    image 'nexus.tkhtechnology.com/amd64/chrome_python:latest'
                    registryUrl 'https://nexus.tkhtechnology.com'
                    registryCredentialsId 'jenkins_office365_account'
                    args '-u root:root'
                    reuseNode true
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