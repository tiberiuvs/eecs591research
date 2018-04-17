#!/bin/bash

sudo cp /etc/network/interfaces_base /etc/network/interfaces
sudo echo -e "\nauto enp0s8\niface enp0s8 inet static\n    address 192.168.15."$1"\n    netmask 255.255.255.0\n    network 192.168.15.0\n    broadcast 192.168.15.0\n    gateway 192.168.15.1\n" >> /etc/network/interfaces

sudo ifdown enp0s8; sudo ifdown enp0s3; sudo ifup enp0s3
cd ~
git clone https://github.com/tiberiuvs/eecs591research.git
sudo ifdown enp0s3; sudo ifdown enp0s8; sudo ifup enp0s8
