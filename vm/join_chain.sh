#!/bin/bash

MULTICHAIN_DIR="/home/eecs591/multichain-1.0.4"
DATA_DIR="$MULTICHAIN_DIR/server_data"
MULTICHAIN_D="$MULTICHAIN_DIR/multichaind"

./connect_internet.sh
sudo apt-get update > /dev/null
./connect_internal.sh
mkdir $DATA_DIR
$MULTCHAIN_D vote_chain@192.168.15.11:8000 -datadir=$DATA_DIR -daemon
