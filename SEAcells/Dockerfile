FROM python:3.8.16-bullseye

ENV DEBIAN_FRONTEND=noninteractive

RUN apt -y update && apt upgrade -y && apt install -y --no-install-recommends apt-utils \
    pkg-config build-essential python3 python3-pip python3-setuptools \
    python3-dev wget software-properties-common libssl-dev curl \ 
    libcurl4-openssl-dev liblapack-dev libopenblas-base libopenblas-dev \ 
    gfortran libpng-dev libcairo2-dev libxml2-dev libfontconfig1-dev libmagick++-dev \
    libpq-dev libhdf5-dev python3-igraph libgeos-dev nano


RUN python -m ensurepip --upgrade
RUN pip install cmake
RUN pip install SEACells
