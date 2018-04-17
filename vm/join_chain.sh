#!/bin/bash

MULTICHAIN_DIR="/home/eecs591/multichain-1.0.4/"

./connect_internet.sh
sudo apt-get update > /dev/null
./connect_internal.sh
mkdir $MULTCHAIN_DIR"server_data"
$MULTCHAIN_DIR"multichaind" vote_chain@192.168.15.11:8000 -datadir=$MULTCHAIN_DIR"server_data" -daemon
