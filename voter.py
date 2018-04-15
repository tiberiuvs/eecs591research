#!/usr/bin/env python
import argparse
import json
import random
import subprocess
import uniqueid as uid


class Voter:
    def __init__(self, template, multichainCLI, datadir, chain, stream, publicKeyFile):
        self.template = template
        self.multichainCLI = multichainCLI
        self.datadir = datadir
        self.chain = chain
        self.stream = stream
        self.publicKeyFile = publicKeyFile
        with open(self.template, 'r') as fd:
            ballotTemplate = json.load(fd)
            self.ballotElections = ballotTemplate['elections']
            self.ballotProps = ballotTemplate['propositions']

    def getEmptyBallot(self):
        return (self.ballotElections, self.ballotProps)

    def processBallot(self, ballot, ticket):
        if not uid.validateIDFromHex(ticket, self.publicKeyFile):
            print('Could not validate ballot/ticket')
            return False
        ballotJson = json.dumps(ballot)
        ballotHex = ballotJson.encode('utf-8').hex()
        args = (self.multichainCLI, self.chain, '-datadir={}'.format(self.datadir),
                'publish', self.stream, ticket[-256:], ballotHex)
        popen = subprocess.Popen(args)
        popen.wait()
        # TODO: schedule so at most one per minute is processed
        return True

    def autoFillBallot(self):
        ballotCopy = {}
        for election in self.ballotElections:
            position = election['position']
            options = []
            for option in election['options']:
                for _, name in option.items():
                    options.append(name)
            ballotCopy[position] = random.choice(options)
        return ballotCopy


def runVoterInterface(args):
    vInstance = Voter(args.template, args.multichainCLI, args.datadir, args.chain,
                      args.stream, args.publicKey)
    # Run the interface indefinitely
    while True:
        # TODO: interactive inputs
        pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the interactive voting application')
    parser.add_argument('template', help='path to the ballot template')
    parser.add_argument('multichainCLI', help='path to the multichain CLI')
    parser.add_argument('datadir', help='path to the multichain data directory')
    parser.add_argument('chain', help='name of the blockchain')
    parser.add_argument('stream', help='name of the blockchain stream')
    parser.add_argument('publickey', help='path to the public key')
    runVoterInterface(parser.parse_args())
