from python:3.7.10-stretch

RUN curl -fsSL https://deb.nodesource.com/setup_11.x | bash -
RUN apt update && apt install -y gcc g++ make build-essential nodejs
RUN npm install -g gulp-cli 

WORKDIR /opt/djangogirls

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./djangogirls/requirements.txt .

RUN pip install -r requirements.txt
