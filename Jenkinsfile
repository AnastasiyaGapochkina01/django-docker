pipeline {
    agent any
    stages {
        stage("Build docker image") {
            steps {
                sh "docker build -t agapochkina/private_registry:django ."
                sh "docker push agapochkina/private_registry:django"
            }
        }
        stage("Run python test") {
            steps {
                //
            }
        }
        stage("Run deploy") {
            steps {
                //
            }
        }
    }
}
