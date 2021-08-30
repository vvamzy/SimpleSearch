    pipeline {
    agent any
    stages {
        stage('Example Stage 1') {
            steps {
                parallel(
                        "step 1": {checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'a4529034-cdfd-4e86-980d-f337bf568a5b', url: 'https://github.com/vvamzy/SimpleSearch.git']]])},
                        "step 2": { echo "world" },
                        "step 3": { echo "world" }
                )
            }
        }
        stage('Example Stage 2') {
            steps {
                parallel(
                        "step 1": {git credentialsId: 'a4529034-cdfd-4e86-980d-f337bf568a5b', url: 'https://github.com/vvamzy/SimpleSearch'},
                        "step 2": {bat 'python Simplesearch.py'},
                        "step 3": { echo "Testing!" }
                )
            }
        }
    }
}
