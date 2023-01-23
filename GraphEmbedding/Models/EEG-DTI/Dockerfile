FROM tensorflow/tensorflow:1.15.5-gpu-py3

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils pkg-config git nano mlocate libprotobuf-dev wget 


RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install bidict  scikit-learn numpy tqdm matplotlib


WORKDIR /
RUN git clone https://github.com/MedicineBiology-AI/EEG-DTI.git
WORKDIR /EEG-DTI 

ADD ./DTI_data/ /EEG-DTI/DTI_data/


