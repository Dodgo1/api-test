pipeline{
    environment {
        KEY = "59e62469a3da06b2a9a30ff73c2c0d05"
    }
    agent{
        label 'jenkins-node-intern'
    }
    stages{
        stage("install dependencies and create .env"){
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
            steps {
                script {
                    sh """
                    pip install pipenv
                    pipenv install
                    cp .env.example .env
                    echo "${KEY}" > .env
                    """
                }
            }
        }
        stage("run tests"){
            steps{
                script{
                    sh """
                    pipenv run pytest test_main.py
                    """
                }
            }
        }
    }
}