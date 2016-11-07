# BUILD LIKE THIS
# sudo docker build -t <image_name>:<version> .
# START LIKE THIS (needs docker.sock to start containers)
# sudo docker run -it -d -v /var/run/docker.sock:/var/run/docker.sock -p <host_ip>:5000 <image_name>:<version>

FROM python:3.5

RUN pip install docker-py
RUN pip install gunicorn
RUN pip install Flask
RUN pip install flask-cors

ADD app.py /

# ENV FLASK_DEBUG 1
ENV FLASK_APP app.py

CMD gunicorn -w 10 -b 0.0.0.0:5000 app:app
