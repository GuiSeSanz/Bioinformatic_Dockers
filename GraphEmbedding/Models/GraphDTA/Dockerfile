FROM ribin7bok/pytorch_geometric:pytorch14_cuda101_cudnn7_geometric
# FROM bitnami/pytorch:latest
# FROM informaticsmatters/rdkit-python3-debian

ENV DEBIAN_FRONTEND=noninteractive
USER root

RUN apt-get update && apt-get install -y --no-install-recommends \
	apt-utils pkg-config build-essential git nano mlocate wget libxrender1 \
	libxext6 

RUN wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py
RUN pip3 install --upgrade pip
RUN pip3 install networkx scipy


RUN mkdir /conda
WORKDIR /conda
RUN wget https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh --no-check-certificate\
	&& bash Anaconda3-2021.11-Linux-x86_64.sh -b && rm -f Anaconda3-2021.11-Linux-x86_64.sh
RUN echo 'PATH="/anaconda3/bin:$PATH"' >> ~/.bashrc

WORKDIR /
RUN git clone https://github.com/thinng/GraphDTA.git
WORKDIR /GraphDTA

RUN pip install torch-scatter torch-sparse torch-cluster torch-spline-conv \ 
	torch-geometric -f https://data.pyg.org/whl/torch-1.10.0+cu113.html

RUN /root/anaconda3/bin/conda init bash 
# RUN /anaconda3/bin/conda create -c conda-forge -n rdkit_4_dti rdkit networkx scipy
# RUN conda activate rdkit_4_dti
# RUN /anaconda3/bin/conda install pyg -c pyg -c conda-forge


# RUN python3 create_data.py
# RUN python3 training.py 0 0 0


#SHELL ["/bin/bash", "-c"]
#
	
	
	# && conda create -n geometric python=3 \
	# && conda activate geometric
	# && conda install -y -c conda-forge rdkit\ 
	# && conda install pytorch torchvision cudatoolkit -c pytorch \
	# && pip install torch-scatter==2.0.5+cu110 -f https://pytorch-geometric.com/whl/torch-1.7.0.html
	# && pip install torch-sparse==2.0.5+cu110 -f https://pytorch-geometric.com/whl/torch-1.7.0.html
	# && pip install torch-cluster==2.0.5+cu110 -f https://pytorch-geometric.com/whl/torch-1.7.0.html
	# && pip install torch-spline-conv==2.0.5+cu110 -f https://pytorch-geometric.com/whl/torch-1.7.0.html





