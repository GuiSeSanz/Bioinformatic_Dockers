FROM ubuntu:latest
# FROM informaticsmatters/rdkit-python3-debian

ENV DEBIAN_FRONTEND=noninteractive

USER root

RUN apt-get update && apt-get install -y --no-install-recommends \
	apt-utils pkg-config build-essential git nano mlocate wget


# WORKDIR /
# RUN git clone https://github.com/thinng/GraphDTA.git
# WORKDIR /GraphDTA
# RUN python3 create_data.py
# RUN python3 training.py 0 0 0


RUN mkdir /conda
WORKDIR /conda
RUN wget https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh --no-check-certificate\
	&& bash Anaconda3-2021.11-Linux-x86_64.sh -b -p $HOME/conda 
RUN export PATH="/root/conda/bin:$PATH" 
RUN echo export PATH="/root/conda/bin:$PATH" >> /root/.bashrc
CMD source /root/.bashrc 
	
	
	
	# && conda create -n geometric python=3 \
	# && conda init bash \
	# && conda install -y -c conda-forge rdkit\ 
	# && conda install pytorch torchvision cudatoolkit -c pytorch \
	# && conda activate geometric \
	# && conda install -y -c conda-forge rdkit \
	# && conda install pytorch torchvision cudatoolkit -c pytorch \
	# && pip install torch-scatter==latest+cu101 -f https://pytorch-geometric.com/whl/torch-1.4.0.html 
# pip install torch-sparse==latest+cu101 -f https://pytorch-geometric.com/whl/torch-1.4.0.html
# pip install torch-cluster==latest+cu101 -f https://pytorch-geometric.com/whl/torch-1.4.0.html
# pip install torch-spline-conv==latest+cu101 -f https://pytorch-geometric.com/whl/torch-1.4.0.html
# pip install torch-geometric







conda config --add channels conda-forge
conda config --set channel_priority strict
conda install rdkit rdkit-dev

conda install -c rdkit rdkit

# conflict for html5lib anaconda-navigator charset-normalizer imagecodecs pyrsistent navigator-updater et_xmlfile idna zope.interface packaging backcall



  - feature:/linux-64::__glibc==2.31=0
  - feature:|@/linux-64::__glibc==2.31=0
  - anaconda==2021.11 -> libgcc-ng==9.3.0=h5101ec6_17 -> __glibc[version='>=2.17']
  - argon2-cffi -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - astropy -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - bitarray -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - blas -> libgfortran-ng -> __glibc[version='>=2.17']
  - blosc -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - bottleneck -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - brotli -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - brotlipy -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - brunsli -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - bzip2 -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - c-ares -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - cairo -> libgcc-ng[version='>=7.3.0'] -> __glibc[version='>=2.17']
  - cffi -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - cfitsio -> libgfortran-ng -> __glibc[version='>=2.17']
  - charls -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - conda-package-handling -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - cryptography -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - curl -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - cython -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - cytoolz -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - daal4py -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - dbus -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - debugpy -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - expat -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - fastcache -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - fontconfig -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - freetype -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - fribidi -> libgcc-ng[version='>=7.5.0'] -> __glibc[version='>=2.17']
  - gevent -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - giflib -> libgcc-ng[version='>=7.5.0'] -> __glibc[version='>=2.17']
  - glib -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - gmp -> libgcc-ng[version='>=7.5.0'] -> __glibc[version='>=2.17']
  - gmpy2 -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - graphite2 -> libgcc-ng[version='>=7.5.0'] -> __glibc[version='>=2.17']
  - greenlet -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - gst-plugins-base -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - gstreamer -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - h5py -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - harfbuzz -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - hdf5 -> libgfortran-ng -> __glibc[version='>=2.17']
  - icu -> libgcc-ng[version='>=7.5.0'] -> __glibc[version='>=2.17']
  - imagecodecs -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - jbig -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - jpeg -> libgcc-ng[version='>=7.5.0'] -> __glibc[version='>=2.17']
  - jxrlib -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - kiwisolver -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - krb5 -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - lazy-object-proxy -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - lcms2 -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - lerc -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - libaec -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - libarchive -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - libcurl -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - libdeflate -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - libedit -> libgcc-ng[version='>=7.5.0'] -> __glibc[version='>=2.17']
  - libev -> libgcc-ng[version='>=7.5.0'] -> __glibc[version='>=2.17']
  - libffi -> libgcc-ng[version='>=7.5.0'] -> __glibc[version='>=2.17']
  - libgcc-ng -> __glibc[version='>=2.17']
  - libgfortran-ng -> __glibc[version='>=2.17']
  - liblief -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - libllvm11 -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - libnghttp2 -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - libpng -> libgcc-ng[version='>=7.5.0'] -> __glibc[version='>=2.17']
  - libsodium -> libgcc-ng[version='>=7.5.0'] -> __glibc[version='>=2.17']
  - libspatialindex -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - libssh2 -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - libstdcxx-ng -> __glibc[version='>=2.17']
  - libtiff -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - libtool -> libgcc-ng[version='>=7.5.0'] -> __glibc[version='>=2.17']
  - libuuid -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - libuv -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - libwebp -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - libwebp-base -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - libxcb -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - libxml2 -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - libxslt -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - libzopfli -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - llvmlite -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - lxml -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - lz4-c -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - lzo -> libgcc-ng[version='>=7.5.0'] -> __glibc[version='>=2.17']
  - markupsafe -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - matplotlib -> libgcc-ng[version='>=7.3.0'] -> __glibc[version='>=2.17']
  - matplotlib-base -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - mistune -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - mkl-service -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - mkl_fft -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - mkl_random -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - mpc -> libgcc-ng[version='>=7.5.0'] -> __glibc[version='>=2.17']
  - mpfr -> libgcc-ng[version='>=7.5.0'] -> __glibc[version='>=2.17']
  - mpich -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - msgpack-python -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - ncurses -> libgcc-ng[version='>=7.5.0'] -> __glibc[version='>=2.17']
  - numba -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - numexpr -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - numpy -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - numpy-base -> libgcc-ng[version='>=7.5.0'] -> __glibc[version='>=2.17']
  - openjpeg -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - openssl -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - pandas -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - pango -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - patchelf -> libgcc-ng[version='>=7.5.0'] -> __glibc[version='>=2.17']
  - pcre -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - pillow -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - pixman -> libgcc-ng[version='>=7.5.0'] -> __glibc[version='>=2.17']
  - psutil -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - py-lief -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - pycosat -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - pycurl -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - pyerfa -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - pyodbc -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - pyqt -> libgcc-ng[version='>=7.5.0'] -> __glibc[version='>=2.17']
  - pyrsistent -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - pytables -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - python=3.9 -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - pywavelets -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - pyyaml -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - pyzmq -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - qt -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - rdkit -> libgcc-ng[version='>=7.3.0'] -> __glibc[version='>=2.17']
  - readline -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - regex -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - ripgrep -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - ruamel_yaml -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - scikit-image -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - scikit-learn -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - scipy -> libgfortran-ng -> __glibc[version='>=2.17']
  - sip -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - snappy -> libgcc-ng[version='>=7.5.0'] -> __glibc[version='>=2.17']
  - sqlalchemy -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - sqlite -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - statsmodels -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - tbb -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - tbb4py -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - tifffile -> libgcc-ng[version='>=7.3.0'] -> __glibc[version='>=2.17']
  - tk -> libgcc-ng[version='>=7.5.0'] -> __glibc[version='>=2.17']
  - tornado -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - typed-ast -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - ujson -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - unixodbc -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - wrapt -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - xz -> libgcc-ng[version='>=7.5.0'] -> __glibc[version='>=2.17']
  - yaml -> libgcc-ng[version='>=7.5.0'] -> __glibc[version='>=2.17']
  - zeromq -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - zfp -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - zlib -> libgcc-ng[version='>=7.5.0'] -> __glibc[version='>=2.17']
  - zope.interface -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - zstd -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']

Your installed version is: 2.31