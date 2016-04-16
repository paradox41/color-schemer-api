FROM python:2.7.10
ENV LANG en_US.UTF-8
# RUN pip install -U git+https://github.com/TomNeyland/resource-alchemy.git
ADD . app
WORKDIR app
RUN pip install -U -e .
WORKDIR /
RUN apt-get install git
RUN git clone https://github.com/TomNeyland/resource-alchemy.git
WORKDIR /resource-alchemy
RUN pip install -U -e .
WORKDIR /usr/src/python/app
