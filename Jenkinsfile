pipeline {
    agent any
    environment {
        HUB_TOKEN=credentials('docker-hub-token')
        HUB_USERNAME=credentials('docker-hub-username')
        WORK_DIR='/opt/deploy/django-docker'
    }
    stages {
        stage("Update local repo") {
            steps {
                sh "cd $WORK_DIR && git checkout master && git pull"
            }
        }

        stage("Build docker image") {
            steps {
                sh "docker login -u $HUB_USERNAME -p $HUB_TOKEN"
                script {
                    sh "cd $WORK_DIR && git log -p -1 | grep commit | awk '{print $2}' | xargs git diff-tree --no-commit-id --name-only -r"
                    // закидвать в файл и если там есть Dockerfile или код - билдить новый образ по хэшу коммита
                }
                sh "cd $WORK_DIR && docker build -t agapochkina/private_registry:django ."
                sh "docker push agapochkina/private_registry:django"
            }
        }
        
      stage("Run python test") {
            steps {
                sh "cd $WORK_DIR && docker-compose up -d"
                sh "docker exec -i django python -m pytest"
                sh "docker ps -a -q | xargs docker stop && docker ps -a -q | xargs docker rm"
            }
        }
        stage("Run deploy") {
            steps {
                sh '''ssh 192.168.56.103 "cd /opt/jenkins-deploy/django-docker && docker-compose up -d"'''
            }
        }
    }
}
