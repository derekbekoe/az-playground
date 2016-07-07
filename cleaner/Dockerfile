# BUILD LIKE THIS
# sudo docker build -t <image_name>:<version> .
# START LIKE THIS (needs docker.sock to start containers)
# sudo docker run -it -d -v /var/run/docker.sock:/var/run/docker.sock <image_name>:<version>

FROM python:3.5

RUN pip install docker-py

ADD job.py /

CMD while true; do python job.py; sleep 60; done
