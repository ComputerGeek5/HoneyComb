#!/bin/bash
#TODO: Make this environment-agnostic as well in the future

docker build -t honeycomb:1.0 .
docker run -d -p 8000:80 --name honeycomb -t honeycomb:1.0