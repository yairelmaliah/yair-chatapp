#!/bin/bash

if ! command -v docker-compose &> /dev/null
then
    echo "docker-compose could not be found in this os, please download it using below command"
    echo "apt-get update -y; apt-get install docker-compose"
    exit 1
fi

docker-compose up --scale app=3 -d --build

echo "Chat app is running..."
echo "please go to - http://localhost to start using this little app :))" 

exit 0