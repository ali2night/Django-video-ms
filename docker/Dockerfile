# pull base image

FROM debian:latest



# Install requirements
RUN apt-get update && apt-get install -y nginx python-pip zlib1g-dev libjpeg-dev python-dev uwsgi 
RUN pip install django
RUN pip install pillow



# Change workdirecotry
WORKDIR /var/www
RUN apt-get install -f -y 
RUN apt-get install -y apt-utils supervisor
# Copy rootfs
COPY rootfs /
# fix permissions
RUN chmod +x /usr/local/bin/start.sh
# run default command
CMD /usr/local/bin/start.sh
