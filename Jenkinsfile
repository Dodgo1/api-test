pipeline{
    agent{
        label 'jenkins-node-intern'
    }
    stages{
        stage("install dependencies"){
            steps{
                sh "pip install pipenv"
                sh "pipenv --version"
            }
        }

        stage("Run test"){
            steps{
                sh """
                pytest test_main.py
                """
            }
        }
    }
}