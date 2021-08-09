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
                sh "cd $TEST_WORK_DIR && git fetch && git reset --hard origin/${branch}"
            }
        }

        stage("Build docker image") {
            steps {
                script {
                   def short_commit = sh (script: "cd $TEST_WORK_DIR && git log -n 1 --pretty=format:'%h'", returnStdout: true ).trim()
                   def changed_files = sh (script: "cd $TEST_WORK_DIR && git diff-tree --no-commit-id --name-only -r $short_commit", returnStdout: true ).trim()
                   docker_tag = "agapochkina/private_registry:django-$branch-$short_commit"
                   sh "cd $TEST_WORK_DIR && echo 'TAG=$branch-$short_commit' > env.dev"
                   if (changed_files.equals("Dockerfile") || changed_files.equals("djangogirls/*")) {
                       echo "Docker image will be rebuild..."
                       //echo "Commit hash: $short_commit"
                       sh "docker login -u $HUB_USERNAME -p $HUB_TOKEN"
                       sh "cd $TEST_WORK_DIR && docker build -t $docker_tag ."
                       sh "docker push $docker_tag"
                   } else {
                       echo "No changes in $short_commit! Docker image will not be rebuild. Exiting..."
                       def skip_next_step = "true"
                       return skip_next_step
                       //error("Exit from pipeline")
                   }
                }
            }
        }
        
        stage("Run python test") {
            steps {
                sh "cd $TEST_WORK_DIR && docker-compose --env-file ./env.dev up -d"
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
