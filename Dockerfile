FROM docker.io/centos/python-36-centos7:latest

RUN mkdir current
COPY requirements.txt .
RUN pip install -r requirements.txt
USER root
RUN yum install mysql -y
