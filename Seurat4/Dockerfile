FROM satijalab/seurat:4.0.5

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils \
    pkg-config build-essential python3.6 python3-pip python3-setuptools \
    python3-dev wget software-properties-common libssl-dev curl \ 
    libcurl4-openssl-dev liblapack-dev libopenblas-base libopenblas-dev \ 
    gfortran libpng-dev libcairo2-dev libxml2-dev libfontconfig1-dev libmagick++-dev \
    libpq-dev libhdf5-dev

RUN R -e "install.packages('reticulate')"

RUN mkdir /JIND_V2
COPY /../../JIND_V2/Extract_data.R /JIND_V2
COPY /home/tereshkova/data/gserranos/JIND_V2/DATA/*.rds /JIND_V2