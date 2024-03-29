FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils \
    pkg-config build-essential python3.6 python3-pip python3-setuptools \
    python3-dev wget software-properties-common libssl-dev curl \
    libcurl4-openssl-dev liblapack-dev libopenblas-base libopenblas-dev \
    gfortran libpng-dev libcairo2-dev libxml2-dev libfontconfig1-dev \
    libmagick++-dev libpq-dev libhdf5-dev git nano

# Install R4
RUN wget -qO- https://cloud.r-project.org/bin/linux/ubuntu/marutter_pubkey.asc | tee -a /etc/apt/trusted.gpg.d/cran_ubuntu_key.asc
RUN add-apt-repository "deb https://cloud.r-project.org/bin/linux/ubuntu $(lsb_release -cs)-cran40/"
RUN apt-get install -y --no-install-recommends r-base r-base-core r-recommended r-base-dev
RUN R -e "install.packages('reticulate', dependencies=TRUE, repos='http://cran.rstudio.com/')"
RUN R -e "install.packages('Seurat', dependencies=TRUE, repos='http://cran.rstudio.com/')"
RUN R -e "install.packages('devtools', dependencies=TRUE, repos='http://cran.rstudio.com/')"

# install python3.6.8
WORKDIR  /opt
RUN wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz
RUN tar xzf Python-3.6.8.tgz
RUN rm -f Python-3.6.8.tgz
WORKDIR  /opt/Python-3.6.8 
RUN ./configure --enable-optimizations && make altinstall

# RUN add-apt-repository ppa:deadsnakes/ppa 
# RUN apt update 
# RUN apt install python3.6-dev

RUN python3.6 -m pip install --upgrade pip

# get the Git repository
WORKDIR /
RUN git clone https://github.com/mohit1997/JIND
WORKDIR /JIND 
RUN python3.6 -m pip install -e .

# set python3.6.8 callable as python 
RUN echo 'alias python="python3.6"' >> ~/.bashrc

WORKDIR /
RUN wget https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh
RUN bash Anaconda3-2021.11-Linux-x86_64.sh -b && rm -f Anaconda3-2021.11-Linux-x86_64.sh


RUN echo 'PATH="/root/anaconda3/bin/conda/bin/:$PATH"' >> ~/.bashrc
SHELL ["/bin/bash", "-c"] 
RUN /root/anaconda3/bin/conda init bash
RUN /root/anaconda3/bin/conda create -n JIND python=3.6.8 -y



