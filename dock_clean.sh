#!/bin/sh

docker images --no-trunc | grep '<none>' | awk '{ print $3 }'  | xargs docker rmi
docker ps --filter status=dead --filter status=exited -aq | xargs docker rm -v

