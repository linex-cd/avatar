#!/bin/bash

#-----------------------------
version=$(cat VERSION)
image_name=$(cat IMAGE)
container_name=$(cat SERVICE)


SERVER_PORT=9009



#-----------------------------
#image
cd ..
cp ./deploy/Dockerfile ./
docker build -f ./Dockerfile -t ${image_name}:${version} .
rm Dockerfile
cd ./deploy




docker run \
--name=${container_name} \
--network=host \
-e SERVER_PORT=${SERVER_PORT} \
--restart=always \
-it ${image_name}:${version} \
bash