FROM python:3.9

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y --no-install-recommends apt-utils libopenmpi-dev \
    pkg-config build-essential python3 python3-pip python3-setuptools \
    python3-dev wget software-properties-common libssl-dev curl \
    libcurl4-openssl-dev liblapack-dev libopenblas-base libopenblas-dev \
    gfortran libpng-dev libcairo2-dev libxml2-dev libfontconfig1-dev \
    cmake libmagick++-dev libpq-dev libhdf5-dev git libgsl-dev locate htop nano

RUN pip install  mpi4py petsc petsc4py slepc slepc4py


RUN pip install 'cellrank[krylov]'
