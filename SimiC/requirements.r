
install.packages("BiocManager")
install.packages('remotes', dependencies=TRUE)
install.packages('reticulate', dependencies=TRUE)
install.packages('dplyr', dependencies=TRUE)
install.packages('future', dependencies=TRUE)
install.packages('viridis', dependencies=TRUE)
install.packages('ggplot2', dependencies=TRUE)

install.packages('plyr', dependencies=TRUE)
install.packages('reshape2', dependencies=TRUE)
install.packages('gridExtra', dependencies=TRUE)
install.packages('ggridges', dependencies=TRUE)
install.packages('stringr', dependencies=TRUE)
install.packages('hues', dependencies=TRUE)
install.packages('pheatmap', dependencies=TRUE)
install.packages('Rtsne', dependencies=TRUE)
install.packages('sitmo', dependencies=TRUE)

install.packages('cowplot', dependencies=TRUE)

install.packages('devtools')
install.packages('https://cran.r-project.org/src/contrib/Archive/rsvd/rsvd_1.0.1.tar.gz', repos = NULL, type="source", upgrade='never')
install.packages('https://cran.r-project.org/src/contrib/Archive/spatstat/spatstat_1.64-1.tar.gz', repos=NULL,type="source", upgrade='never')
devtools::install_version(package = 'Seurat', version = package_version('3.2.3'), upgrade='never')

