#!/usr/bin/env bash
set -e

add-apt-repository ppa:ubuntugis/ppa
apt-get update
apt-get -y install gdal-bin
apt-get -y install libgdal-dev
export CPLUS_INCLUDE_PATH=/usr/include/gdal
export C_INCLUDE_PATH=/usr/include/gdal
pip install GDAL