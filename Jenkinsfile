peline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'a4529034-cdfd-4e86-980d-f337bf568a5b', url: 'https://github.com/vvamzy/SimpleSearch.git']]])
            }
        }
        stage('Build') {
            git credentialsId: 'a4529034-cdfd-4e86-980d-f337bf568a5b', url: 'https://github.com/vvamzy/SimpleSearch'
            bat 'python Simplesearch.py'
        }
        stage('Test') {
            steps {
                echo 'Testing in Progress!'
            }
        }
    }
}

