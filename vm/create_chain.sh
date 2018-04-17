#!/bin/bash

MULTICHAIN_DIR="/home/eecs591/multichain-1.0.4/"

./connect_internet.sh
sudo apt-get update > /dev/null
./connect_internal.sh
mkdir $MULTCHAIN_DIR"server_data"
$MULTCHAIN_DIR"multichain-util" create vote_chain -datadir=$MULTCHAIN_DIR"server_data" -default-network-port=8000 -anyone-can-connect=true -anyone-can-send=true -anyone-can-receive=true -root-stream-name=voting_stream -root-stream-open=true
$MULTCHAIN_DIR"multichaind" vote_chain -datadir=$MULTCHAIN_DIR"server_data" -daemon
