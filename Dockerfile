FROM ubuntu:16.04

WORKDIR /vip_admin
RUN apt-get update -y;apt-get install -y python python3.5 python3-pip \
		python-pip tzdata libxml2 apt-utils sqlite3 build-essential;
RUN pip install --upgrade pip
RUN echo "Asia/Tehran" > /etc/timezone
RUN echo "dns-nameservers 94.232.174.194"  >> /etc/network/interfaces
ENV TZ=Asia/Tehran
COPY ./requirements.txt ./requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY ./ ./
RUN pip3 install -e .
CMD vip_admin start

