# Install - Docker
Run install.sh to create the docker image and start the container. If you want to change the ports where the services
are running you have to edit the docker run command in docker_install.sh like shown below:

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

You can delete the docker container and image associated with it by running the docker_uninstall.sh script.

# Install - Linux
Give execute permissions to linux_install.sh and run it as root. After that run main.py as root as well. 
For example:

```console
chmod +x linux_install.sh
sudo /usr/bin/bash linux_install.sh
sudo /usr/bin/python3.10 main.py
```
