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


# import scvi
# import scanpy as sc
# adata = sc.read_text('hemato_data_raw.txt', delimiter = '\t')
# sc.pp.filter_genes(adata, min_counts=3)
# adata.layers["counts"] = adata.X.copy()
# sc.pp.normalize_total(adata, target_sum=1e4)
# sc.pp.log1p(adata)
# adata.raw = adata # freeze the state in `.raw`
# sc.pp.highly_variable_genes(
#     adata, 
#     n_top_genes=1200, 
#     subset=True, 
#     layer="counts", 
#     flavor="seurat_v3",
# )
# scvi.model.SCVI.setup_anndata(
#     adata,
#     layer="counts"
# )
# model = scvi.model.SCVI(adata)
# model.train()


# adata.obsm["X_scVI"] = model.get_latent_representation()
# adata.obsm["X_normalized_scVI"] = model.get_normalized_expression()