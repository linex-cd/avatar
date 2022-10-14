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

#make dir for data
if [ ! -d "/data" ]; then
	echo 'Making path (/data) for cache...'
	mkdir /data
fi

if [ ! -d "/data/fsa" ]; then
	echo 'Making path (/data/fsa) for cache...'
	mkdir /data/fsa
fi

if [ ! -d "/data/fsa/data" ]; then
	echo 'Making path (/data/fsa/data) for cache...'
	mkdir /data/fsa/data
fi

docker run \
--name=${container_name} \
--network=host \
-e SERVER_PORT=${SERVER_PORT} \
-v /data/fsa/data/:/data \
--restart=always \
-d ${image_name}:${version} \
python3 main.py