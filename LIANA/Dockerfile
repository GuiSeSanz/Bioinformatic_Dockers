FROM satijalab/seurat:4.0.5

ENV DEBIAN_FRONTEND=noninteractive

RUN apt -y update && apt upgrade -y && apt install -y --no-install-recommends apt-utils \
    pkg-config build-essential python3 python3-pip python3-setuptools \
    python3-dev wget software-properties-common libssl-dev curl \ 
    libcurl4-openssl-dev liblapack-dev libopenblas-base libopenblas-dev \ 
    gfortran libpng-dev libcairo2-dev libxml2-dev libfontconfig1-dev libmagick++-dev \
    libpq-dev libhdf5-dev python3-igraph libgeos-dev nano

RUN Rscript --vanilla -e 'install.packages("remotes" ,repos = "http://cran.us.r-project.org")'
# # LIANA dependencies
RUN Rscript --vanilla -e 'remotes::install_github("raivokolde/RobustRankAggreg")'
RUN Rscript --vanilla -e 'install.packages("rgeos",repos = "http://cran.us.r-project.org")'
RUN Rscript --vanilla -e 'install.packages("SeuratObject",repos = "http://cran.us.r-project.org")'
RUN Rscript --vanilla -e 'install.packages("tidyverse",repos = "http://cran.us.r-project.org")'
RUN wget  https://bioconductor.org/packages/3.13/bioc/src/contrib/ScaledMatrix_1.0.0.tar.gz && Rscript --vanilla -e 'install.packages("ScaledMatrix_1.0.0.tar.gz",repos = NULL, type = "source")'

RUN wget https://bioconductor.org/packages/3.14/bioc/src/contrib/BiocSingular_1.10.0.tar.gz && Rscript --vanilla -e 'install.packages("BiocSingular_1.10.0.tar.gz",repos = NULL, type = "source")'
RUN wget https://mghp.osn.xsede.org/bir190004-bucket01/archive.bioconductor.org/packages/3.13/bioc/src/contrib/sparseMatrixStats_1.4.2.tar.gz && Rscript --vanilla -e 'install.packages("sparseMatrixStats_1.4.2.tar.gz",repos = NULL, type = "source")'
RUN wget https://bioconductor.org/packages/3.13/bioc/src/contrib/DelayedMatrixStats_1.14.3.tar.gz && Rscript --vanilla -e 'install.packages("DelayedMatrixStats_1.14.3.tar.gz",repos = NULL, type = "source")'
RUN wget https://mghp.osn.xsede.org/bir190004-bucket01/archive.bioconductor.org/packages/3.13/bioc/src/contrib/metapod_1.0.0.tar.gz && Rscript --vanilla -e 'install.packages("metapod_1.0.0.tar.gz",repos = NULL, type = "source")'


# R to python and back
RUN Rscript --vanilla -e 'install.packages("reticulate",repos = "http://cran.us.r-project.org")'
RUN pip3 install rpy2
RUN Rscript --vanilla -e 'BiocManager::install("BiocSingular")'
RUN Rscript --vanilla -e 'BiocManager::install("bluster")'
RUN Rscript --vanilla -e 'BiocManager::install("scran")'
RUN Rscript --vanilla -e 'BiocManager::install("scater")'
RUN Rscript --vanilla -e 'BiocManager::install("scuttle")'
# # # Install LIANA
RUN Rscript --vanilla -e 'remotes::install_github("saezlab/liana")'
