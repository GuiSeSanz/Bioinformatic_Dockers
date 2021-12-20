FROM tensorflow/tensorflow:1.14.0-gpu-py3

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils pkg-config git nano mlocate libprotobuf-dev


RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install bidict  scikit-learn numpy tqdm


WORKDIR /
RUN git clone https://github.com/samehkamaleldin/libkge.git
WORKDIR /libkge 
RUN python3 -m pip install numpy --upgrade
RUN python3 -m pip install numba
RUN python3 -m pip install -r requirements.txt
RUN python setup.py install
#Test run 
WORKDIR /libkge/examples/
RUN python3 kge_model_pipeline.py
WORKDIR /
RUN git clone https://github.com/samehkamaleldin/bio-kge-apps.git

### The line containing         
#       X_res, y_res= sm.fit_sample(X_train_transform, YY[train_index])
#       must be replaced with
#       X_res, y_res= sm.fit_resample(X_train_transform, YY[train_index])



