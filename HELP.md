# Install - Docker
Run install.sh to create the docker image and start the container. If you want to change the ports where the services
are running you have to edit the docker run command in install.sh like shown below:

```console
docker run -d -p <YOUR_PORT>:80 ... 
```

and the EXPOSE commands in the Dockerfile like shown below:

```console
EXPOSE 80
EXPOSE 21
...
```

# Uninstall - Docker

You can delete the docker container and image associated with it by running the uninstall.sh script.

# Install - Linux
Run the configure.sh with a shell of your choice script and then run main.py with the python command