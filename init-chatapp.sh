#!/bin/bash

# Check if user can 
if ! command -v docker-compose &> /dev/null
then
    echo "docker-compose could not be found in this os, please download it using below command"
    echo "sudo apt-get update -y; sudo apt-get install docker-compose"
    exit 1
fi

# Run containers
docker-compose up --scale app=3 -d --build
if [ $? -eq 0 ]; then 
    echo -e "\n====================="
    echo "Chat app is running..."
    echo "please go to - http://localhost to start using this little app :))" 
    echo -e "====================="
    exit 0
fi
