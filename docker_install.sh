#!/bin/bash
#TODO: Make this environment-agnostic as well in the future

docker build -t honeycomb:1.0 .
docker run -d -p 80:80 -p 21:21 -p 23:23 --name honeycomb -t honeycomb:1.0