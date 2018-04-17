#!/bin/bash

MULTICHAIN_DIR="/home/eecs591/multichain-1.0.4/"

killall multichaind
rm -r $MULTICHAIN_DIR"server_data"
