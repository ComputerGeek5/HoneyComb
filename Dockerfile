FROM python:3.10-alpine

WORKDIR /root/honeycomb

#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 80

RUN chmod +x configure.sh
#TODO: configure.sh doesn't seem to be executing, Alpine uses /bin/sh instead of bash so we have to install it with apt: https://stackoverflow.com/questions/40944479/docker-how-to-use-bash-with-an-alpine-based-docker-image
#CMD [ "/bin/sh", "configure.sh" ]

RUN chmod +x main.py
ENTRYPOINT [ "python3", "main.py" ]