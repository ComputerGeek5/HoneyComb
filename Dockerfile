FROM python:3.10-alpine

WORKDIR /root/honeycomb

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 80
EXPOSE 21

RUN chmod +x configure.sh
#TODO: Make the script environment-agnostic in the future
RUN /bin/sh configure.sh

RUN chmod +x main.py
ENTRYPOINT [ "python3", "main.py" ]