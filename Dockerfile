FROM python:3.8-slim

USER root


RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    wget \
    unzip \
    xvfb \
    libxi6 \
    libgconf-2-4 \
    python3.11-venv



RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add && bash -c "echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' >> /etc/apt/sources.list.d/google-chrome.list" && apt-get -y update && apt-get -y install google-chrome-stable


RUN wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/116.0.5845.96/linux64/chromedriver-linux64.zip && unzip chromedriver-linux64.zip && mv chromedriver-linux64/chromedriver /usr/bin/chromedriver && chown root:root /usr/bin/chromedriver && chmod +x /usr/bin/chromedriver




WORKDIR /app

COPY ./salespredictiontest.py /app/
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt



CMD [ "python3","salespredictiontest.py"]




