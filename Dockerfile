# Image tag
FROM python:3.10.4

RUN mkdir /VNDBScraper

WORKDIR /VNDBScraper

#COPY FROM - TO
COPY . .

# The following commands are copied from docker_selenium.md
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# Download chromedriver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN apt-get install -yqq unzip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

#Install all the dependencies for our code
RUN pip install -r requirements.txt

#When we run container, this is the command to be run
ENTRYPOINT ["python3", "VNDBScraper.py"]