#!/usr/bin/env python
import argparse
import uniqueid as uid
import voter


parser = argparse.ArgumentParser(description='Run the testing application for the voting system')
parser.add_argument('-t','--template', help='path to the ballot template',
                    default='data/paper_ballot.json')
parser.add_argument('-m','--multichain', help='path to the multichain CLI',
                    default='../multichain-1.0.4/multichain-cli')
parser.add_argument('-d','--datadir', help='path to the multichain data directory',
                    default='../multichain-1.0.4/server_data')
parser.add_argument('-c','--chain', help='name of the blockchain',
                    default='vote_chain')
parser.add_argument('-s','--stream', help='name of the blockchain stream',
                    default='voting_stream')
parser.add_argument('-p','--publickey', help='path to the public key',
                    default='data/publickey.der')
parser.add_argument('-r','--privatekey', help='path to the private key',
                    default='data/privatekey.p8')
args = parser.parse_args()

vInstance = voter.Voter(args.template, args.multichain, args.datadir, args.chain, args.stream, args.publickey)

for i in range(100):
    newID = uid.generateID(args.privatekey)
    ballot = vInstance.autoFillBallot()
    vInstance.processBallot(ballot, newID)
