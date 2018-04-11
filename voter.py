#!/usr/bin/env python
import json
import random
import subprocess
import uniqueid as uid


class Voter:
    def __init__(self):
        self.TEMPLATE_LOCATION = 'data/paper_ballot.json' 
        self.MULTICHAIN_DIR = '../multichaind'
        self.DATA_DIR = 'server_data'
        self.CHAIN_NAME = 'election_chain'
        self.ELECTIONS_KEY = 'elections'
        self.POSITION_KEY = 'position'
        self.OPTIONS_KEY = 'options'
        self.WRITEIN_KEY = 'writein'
        self.PROPOSITIONS_KEY = 'propositions'
        self.PUBLISH_CMD = 'publish'
        self.STREAM_NAME = 'root'
        self.loadBallotTemplate()
        self.runBlockchain()

    def loadBallotTemplate(self):
        with open(self.TEMPLATE_LOCATION, 'r') as fd:
            ballotTemplate = json.load(fd)
            self.ballotElections = ballotTemplate[self.ELECTIONS_KEY]
            self.ballotProps = ballotTemplate[self.PROPOSITIONS_KEY]

    def runBlockchain(self):    
        # Now that the permission has been granted, connect to the master server
        args = (self.MULTICHAIN_DIR, self.CHAIN_NAME,
                '-datadir=' + self.DATA_DIR, '-daemon')
        popen = subprocess.Popen(args)
        popen.wait()

    def processBallot(self, ballot, ticket):
        ballotJson = json.dumps(ballot)
        ballotHex = ballotJson.encode('utf-8').hex()
        print(ballotHex)
        # TODO: load into blockchain!
        args = (self.PUBLISH_CMD, self.STREAM_NAME, ticket, ballotHex)
        popen = subprocess.Popen(args)
        popen.wait()

    def getID(self):
        return 'faketicket'

    def createBallotAuto(self):
        ballotCopy = {}
        for election in self.ballotElections:
            position = election[self.POSITION_KEY]
            options = []
            for option in election[self.OPTIONS_KEY]:
                for _, name in option.items():
                    options.append(name)
            ballotCopy[position] = random.choice(options)
        return ballotCopy

    def createBallot(self):
        pass
            
    def run(self):
        ballot = self.createBallotAuto()
        ticket = self.getID()
        self.processBallot(ballot, ticket)


if __name__ == '__main__':
    voter = Voter()
    voter.run()
