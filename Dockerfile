# Image tag
FROM python:3.10.4

RUN mkdir /VNDBScraper

WORKDIR /VNDBScraper

#COPY FROM - TO
COPY . .

# Install all the dependencies
#RUN pip install -r requirements.txt

#Maybe need to install chromedriver?
#RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
#RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
#RUN apt-get -y update
#RUN apt-get install -y google-chrome-stable

#When we run container, this is the command to be run
ENTRYPOINT ["python3", "VNDBScraper.py"]