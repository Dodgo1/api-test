pipeline{
    agent{
        label 'jenkins-node-intern'
    }
    stages{
        stage("install dependencies"){
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
                        pipenv install --dev
                        pipenv run pytest tests/ -vs --headless --junitxml=result.xml
                        """
                    }
                }

        }
    }
}