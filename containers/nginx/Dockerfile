FROM ubuntu:xenial

RUN apt-get update && \
    apt-get install -y nginx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
# ADD sites-enabled/ /etc/nginx/sites-enabled
RUN rm /etc/nginx/sites-enabled/default
RUN mkdir /www /www/static

EXPOSE 443

CMD ["/usr/sbin/nginx"]
