#!/bin/bash

version=$(cat VERSION)
image_name=$(cat IMAGE)
container_name=$(cat SERVICE)


docker stop ${container_name}
docker rm  ${container_name}

docker rmi  ${image_name}:${version}