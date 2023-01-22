#!/bin/bash
#TODO: Make this environment-agnostic as well in the future

docker rm -f honeycomb
docker rmi honeycomb:1.0