FROM debian:8
MAINTAINER Insight Software Consortium <community@itk.org>

RUN apt-get update && apt-get install -y \
  build-essential \
  curl \
  git \
  libexpat1-dev \
  libcurl4-openssl-dev \
  libssl-dev \
  libhdf5-dev \
  libjpeg-dev \
  libpng12-dev \
  libpython3-dev \
  libtiff5-dev \
  python3 \
  ninja-build \
  wget \
  vim \
  zlib1g-dev

RUN mkdir -p /usr/src/ITKRLEImage-build
WORKDIR /usr/src

RUN git clone git://cmake.org/cmake.git CMake && \
  cd CMake && \
  git checkout v3.11.1 && \
  cd .. && mkdir CMake-build && cd CMake-build && \
  /usr/src/CMake/bootstrap \
    --parallel=$(nproc) \
    --prefix=/usr && \
  make -j$(nproc) && \
  ./bin/cmake -DCMAKE_USE_SYSTEM_CURL:BOOL=ON \
    -DCMAKE_BUILD_TYPE:STRING=Release \
    -DCMAKE_USE_OPENSSL:BOOL=ON . && \
  make install && \
  cd .. && \
  rm -rf CMake*

# ITK master 2018-05-15
ENV ITK_GIT_TAG aa57caf04732f8c0b56f575b65c532e107720e49
RUN git clone https://itk.org/ITK.git && \
  cd ITK && \
  git checkout ${ITK_GIT_TAG} && \
  cd ../ && \
  mkdir ITK-build && \
  cd ITK-build && \
  cmake \
    -G Ninja \
    -DCMAKE_INSTALL_PREFIX:PATH=/usr \
    -DCMAKE_BUILD_TYPE:STRING=Release \
    -DBUILD_EXAMPLES:BOOL=OFF \
    -DBUILD_TESTING:BOOL=OFF \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DITK_LEGACY_REMOVE:BOOL=ON \
    -DITK_BUILD_DEFAULT_MODULES:BOOL=OFF \
    -DITK_USE_SYSTEM_LIBRARIES:BOOL=ON \
    -DModule_ITKCommon:BOOL=ON \
    -DModule_ITKImageGrid:BOOL=ON \
    -DModule_ITKIOImageBase:BOOL=ON \
    -DModule_ITKTestKernel:BOOL=ON \
  ../ITK && \
  ninja && \
  find . -name '*.o' -delete
