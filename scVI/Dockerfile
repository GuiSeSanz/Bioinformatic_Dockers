# FROM ubuntu:latest

FROM pytorch/pytorch:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils \
    pkg-config build-essential \
    python3-dev wget software-properties-common libssl-dev curl \
    libcurl4-openssl-dev liblapack-dev libopenblas-base libopenblas-dev \
    gfortran libpng-dev libcairo2-dev libxml2-dev libfontconfig1-dev \
    libmagick++-dev libpq-dev libhdf5-dev git libgsl-dev locate

# Install R4
RUN wget -qO- https://cloud.r-project.org/bin/linux/ubuntu/marutter_pubkey.asc | tee -a /etc/apt/trusted.gpg.d/cran_ubuntu_key.asc
RUN add-apt-repository "deb https://cloud.r-project.org/bin/linux/ubuntu $(lsb_release -cs)-cran40/"

RUN apt-get install -y --no-install-recommends r-base r-base-core r-recommended r-base-dev

RUN pip install scvi-tools
RUN pip install scanpy
RUN pip install scikit-misc
COPY hemato_data_raw.txt /workspace
COPY LaunchscVI.py /workspace
