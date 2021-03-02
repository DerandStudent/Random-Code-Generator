#!/bin/bash
#taken from a template & changed
scp -i ~/.ssh/id_rsa docker-compose.yaml jenkins@swarm-manager:/home/jenkins/docker-compose.yaml
ssh -i ~/.ssh/id_rsa jenkins@swarm-manager << EOF
    export DATABASE_URI=${DATABASE_URI}
    export AUTHOR=${AUTHOR}
    docker stack deploy --compose-file /home/jenkins/docker-compose.yaml random_code_generator-stack
EOF