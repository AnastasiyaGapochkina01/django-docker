#!/bin/bash

DEPLOY_USER='gitlab-runner'
DEPLOY_HOST='192.168.56.103'
PROJECT_PATH='/opt/deploy/django-docker'

ssh -o StrictHostKeyChecking=no ${DEPLOY_USER}@${DEPLOY_HOST} "cd ${PROJECT_PATH} && \
                                                               git checkout master && \
                                                               git pull && \
                                                               docker-compose up -d && \
                                                               docker exec -i django python -m pytest"
