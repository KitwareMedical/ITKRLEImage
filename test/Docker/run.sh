#!/bin/sh

script_dir="`cd $(dirname $0); pwd`"

docker run \
  --rm \
  -v $script_dir/../..:/usr/src/ITKRLEImage \
    kitwaremedical/rleimage-test \
      /usr/src/ITKRLEImage/test/Docker/test.sh
