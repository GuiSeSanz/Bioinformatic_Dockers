FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
	apt-utils pkg-config build-essential python3.10 python3-pip \ 
	python3-setuptools python3-dev wget software-properties-common \ 
	libssl-dev curl libcurl4-openssl-dev liblapack-dev libopenblas-base \
	libopenblas-dev gfortran libpng-dev libcairo2-dev libxml2-dev \
	libfontconfig1-dev libmagick++-dev libpq-dev libhdf5-dev git nano mlocate


WORKDIR /
RUN git clone https://github.com/masashitsubaki/CPI_prediction.git
WORKDIR /CPI_prediction

RUN pip3 install torch==1.10.0+cpu torchvision==0.11.1+cpu \
torchaudio==0.10.0+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html

RUN python3 -m pip install scikit-learn RDKit