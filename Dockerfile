FROM node:latest

ENV LANG en_US.UTF-8

ADD . app
WORKDIR app

EXPOSE 3030
