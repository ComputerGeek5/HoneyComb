# Install using docker
Run install.sh, note that it will expose the service in port 8000 on your machine, you can change the docker run command
in install.sh like shown below:

```console
docker run -d -p <YOUR_PORT>:80 ... 
```

Additionally, you can delete the docker container and image associated with it by running the uninstall.sh script.

# Install in Linux
Run the configure.sh with a shell of your choice script and then run main.py with the python command