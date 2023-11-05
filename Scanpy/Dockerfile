FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils \
    pkg-config build-essential \
    python3-dev wget software-properties-common libssl-dev curl \
    libcurl4-openssl-dev liblapack-dev libopenblas-base libopenblas-dev \
    gfortran libpng-dev libcairo2-dev libxml2-dev libfontconfig1-dev \
    libmagick++-dev libpq-dev libhdf5-dev git libgsl-dev locate unzip


RUN wget https://bootstrap.pypa.io/get-pip.py 
RUN python3 ./get-pip.py
RUN pip3 install scanpy

RUN pip3 install tf-nightly tfp-nightly tensorflow tensorflow-probability

RUN 
RUN mkdir /home/scanpy
RUN mkdir /home/scanpy/batchglm
WORKDIR /home/scanpy/batchglm
RUN wget https://github.com/theislab/batchglm/archive/refs/heads/master.zip
RUN unzip master.zip
WORKDIR /home/scanpy/batchglm/batchglm-master
RUN pip3 install -r requirements.txt
RUN pip3 install -e .

##### UNABLE TO INSTALL diffxpy
# RUN mkdir /home/scanpy/diffxpy
# WORKDIR /home/scanpy/diffxpy
# RUN wget https://github.com/theislab/diffxpy/archive/refs/heads/master.zip
# RUN unzip master.zip
# WORKDIR /home/scanpy/diffxpy/diffxpy-master


