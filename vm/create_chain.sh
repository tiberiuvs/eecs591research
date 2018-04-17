#!/bin/bash

MULTICHAIN_DIR="/home/eecs591/multichain-1.0.4"
DATA_DIR="$MULTICHAIN_DIR/server_data"
MULTICHAIN_UTIL="$MULTICHAIN_DIR/multichain-util"
MULTICHAIN_D="$MULTICHAIN_DIR/multichaind"

sudo ifdown enp0s8; sudo ifdown enp0s3; sudo ifup enp0s3
sudo apt-get update > /dev/null
sudo ifdown enp0s3; sudo ifdown enp0s8; sudo ifup enp0s8
mkdir $DATA_DIR
$MULTICHAIN_UTIL create vote_chain -datadir=$DATA_DIR -default-network-port=8000 -anyone-can-connect=true -anyone-can-send=true -anyone-can-receive=true -root-stream-name=voting_stream -root-stream-open=true
$MULTICHAIN_D vote_chain -datadir=$DATA_DIR -daemon
