#!/bin/bash

MULTICHAIN_DIR="/home/eecs591/multichain-1.0.4/"

./connect_internet.sh
sudo apt-get update > /dev/null
./connect_internal.sh
mkdir $MULTCHAINDIR"server_data"
$MULTCHAINDIR"multichaind" vote_chain@192.168.15.11:8000 -datadir=$MULTCHAINDIR"server_data" -daemon
