FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils \
    pkg-config build-essential python3-pip python3-setuptools \
    python3-dev wget software-properties-common libssl-dev curl \
    libcurl4-openssl-dev liblapack-dev libopenblas-base libopenblas-dev \
    gfortran libpng-dev libcairo2-dev libxml2-dev libfontconfig1-dev \
    libmagick++-dev libpq-dev libhdf5-dev git nano

RUN wget -qO- https://cloud.r-project.org/bin/linux/ubuntu/marutter_pubkey.asc | tee -a /etc/apt/trusted.gpg.d/cran_ubuntu_key.asc
RUN add-apt-repository "deb https://cloud.r-project.org/bin/linux/ubuntu $(lsb_release -cs)-cran40/"
RUN apt-get install -y --no-install-recommends r-base r-base-core r-recommended r-base-dev
RUN R -e "install.packages('reticulate', dependencies=TRUE, repos='http://cran.rstudio.com/')"
RUN R -e "install.packages('Seurat', dependencies=TRUE, repos='http://cran.rstudio.com/')"
RUN R -e "install.packages('devtools', dependencies=TRUE, repos='http://cran.rstudio.com/')"

WORKDIR /
RUN wget https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh
RUN bash Anaconda3-2021.11-Linux-x86_64.sh -b && rm -f Anaconda3-2021.11-Linux-x86_64.sh

RUN /root/anaconda3/bin/conda init bash

RUN git clone https://github.com/mohit1997/JIND
WORKDIR /JIND 
RUN pip install -r requirements.txt
RUN pip install -e .

