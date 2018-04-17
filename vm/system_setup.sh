#!/bin/bash

sudo ifdown enp0s8; sudo ifdown enp0s3; sudo ifup enp0s3
cd ~
git clone https://github.com/tiberiuvs/eecs591research.git
sudo ifdown enp0s3; sudo ifdown enp0s8; sudo ifup enp0s8
