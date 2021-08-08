pipeline {
    agent any
    parameters {
        string (
            defaultValue: '',
            description: 'branch to build',
            name: 'branch'
        )
    }
    environment {
        HUB_TOKEN=credentials('docker-hub-token')
        HUB_USERNAME=credentials('docker-hub-username')
        TEST_WORK_DIR='/opt/deploy/django-docker'
        DEPLOY_WORK_DIR='/opt/jenkins-deploy/django-docker'
        STAGING_IP='192.168.56.10X'
        PROD_IP='192.168.56.103'
    }

    stages {
        stage("Update local repo") {
            steps {
                sh "cd $TEST_WORK_DIR && git checkout ${branch} && git pull"
            }
        }

        stage("Build docker image") {
            steps {
                script {
                   def changed_files = sh (script: "cd $TEST_WORK_DIR && git log -p -1 | head -n1 |cut -d ' ' -f 2 | xargs git diff-tree --no-commit-id --name-only -r", returnStdout: true ).trim()
                   echo "Changed files is: changed_files"
                   if (changed_files.equals("Dockerfile") || changed_files.equals("djangogirls/*")) {
                       echo "Docker image will be rebuild..."
                       sh "docker login -u $HUB_USERNAME -p $HUB_TOKEN"
                       sh "cd $TEST_WORK_DIR && docker build -t agapochkina/private_registry:django ."
                       sh "docker push agapochkina/private_registry:django"
                   } else {
                       echo "No changes! Docker image will not be rebuild. Exiting..."
                       error("Exit from pipeline")
                   }
                }
            }
        }
        
        stage("Run python test") {
            steps {
                sh "cd $TEST_WORK_DIR && docker-compose up -d"
                sh "docker exec -i django python -m pytest"
                sh "docker ps -a -q | xargs docker stop && docker ps -a -q | xargs docker rm"
            }
        }

        //stage("Run deploy") {
        //    steps {
        //        sh '''ssh $PROD_IP "cd $DEPLOY_WORK_DIR && docker-compose up -d"'''
        //    }
       // }
    }
}
