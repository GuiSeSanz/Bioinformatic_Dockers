FROM python:3.6.8

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \ 
    apt-utils pkg-config build-essential wget software-properties-common \
    libssl-dev curl libcurl4-openssl-dev liblapack-dev libopenblas-base \
    libopenblas-dev gfortran libpng-dev libcairo2-dev libxml2-dev \ 
    libfontconfig1-dev libmagick++-dev libpq-dev libhdf5-dev git nano locate

# Install R4
RUN wget -qO- https://cloud.r-project.org/bin/linux/ubuntu/marutter_pubkey.asc | tee -a /etc/apt/trusted.gpg.d/cran_ubuntu_key.asc
RUN add-apt-repository "deb https://cloud.r-project.org/bin/linux/ubuntu $(lsb_release -cs)-cran40/"
RUN apt-get install -y --no-install-recommends r-base r-base-core r-recommended r-base-dev


RUN pip3 install --upgrade pip

# get the Git repository
WORKDIR /
RUN git clone https://github.com/mohit1997/JIND
WORKDIR /JIND
RUN pip3 install -e .


RUN R -e "install.packages('reticulate', dependencies=TRUE, repos='http://cran.rstudio.com/')"



# library(reticulate)
# reticulate::use_python("/usr/local/bin/python")
# reticulate::py_config()