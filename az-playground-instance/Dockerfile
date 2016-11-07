# BUILD LIKE THIS
# sudo docker build -t <image_name>:<version> .
# START LIKE THIS
# sudo docker run -it -d -p <host_ip>:3000 <image_name>:<version>

FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y git
RUN git clone https://github.com/sourcelair/xterm.js.git xtermjs; cd xtermjs; git reset --hard 838c11b69c1f7f610eed426035b7dfe391803e87; cd -
# Install xterm, az, jpterm dependencies
RUN apt-get install -y nodejs-legacy npm curl libssl-dev libffi-dev python-dev build-essential python-pip

# Install xterm
WORKDIR xtermjs
RUN npm --logevel=error install

RUN pip install --upgrade pip jmespath-terminal azure-cli

WORKDIR /
# Override demo index.html file with our own
ADD index.html /xtermjs/demo/index.html
ADD style.css /xtermjs/demo/style.css
ADD markdown.css /tmp/markdown.css
RUN cat /tmp/markdown.css >> /xtermjs/demo/style.css

# Remove executables we don't want users to be able to run
# RUN rm /usr/bin/apt-get /bin/ls /bin/cat /usr/bin/whoami /usr/bin/ssh
CMD node xtermjs/demo/app
