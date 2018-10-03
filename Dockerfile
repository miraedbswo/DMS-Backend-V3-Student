FROM rackspacedot/python37
MAINTAINER Nerd-Bear "python@istruly.sexy"

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY Server /app
WORKDIR /app

RUN pip3 install -r requirements.txt
CMD ["python3", "Server/server.py"]