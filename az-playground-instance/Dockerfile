# BUILD LIKE THIS
# sudo docker build -t <image_name>:<version> .
# START LIKE THIS
# sudo docker run -it -d -p <host_ip>:3000 <image_name>:<version>

FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y git
RUN git clone https://github.com/sourcelair/xterm.js.git xtermjs
# Install xterm dependencies
RUN apt-get install -y nodejs-legacy npm
# Install az dependencies
RUN apt-get install -y curl libssl-dev libffi-dev python-dev build-essential
# Install jpterm dependencies
RUN apt-get install -y python-pip

# Install xterm
WORKDIR xtermjs
RUN npm --logevel=error install

# Install az with tab completion
RUN curl -sSL https://aka.ms/projectazinstall -o /tmp/az_install
ENV AZURE_CLI_DISABLE_PROMPTS 1
RUN bash /tmp/az_install
RUN curl -s http://azure-cli-nightly.westus.cloudapp.azure.com/verified/setup_completion.py -o /tmp/az_completion
RUN python /tmp/az_completion /usr/local/az

# Install jpterm
RUN pip install --upgrade pip
RUN pip install jmespath-terminal

WORKDIR /

# Override demo index.html file with our own
ADD index.html /xtermjs/demo/index.html
ADD style.css /xtermjs/demo/style.css
ADD markdown.css /tmp/markdown.css
RUN cat /tmp/markdown.css >> /xtermjs/demo/style.css

# Remove executables we don't want users to be able to run
# RUN rm /usr/bin/apt-get /bin/ls /bin/cat /usr/bin/whoami /usr/bin/ssh
CMD node xtermjs/demo/app

