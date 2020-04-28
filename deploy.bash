#!/bin/bash
while getopts i:u:r:p:s: option
do
case "${option}"
in
u) USER=${OPTARG};;
p) PASSWORD=${OPTARG};;
r) REGISTRY=${OPTARG};;
i) IMAGE=${OPTARG};;
esac
done
docker login -u $USER -p $PASSWORD $REGISTRY
if docker ps | grep -q app
then
docker kill -s HUP app
fi
cd /usr/app/source
docker-compose pull
docker-compose up --build -d
docker container prune -f
docker image prune -f