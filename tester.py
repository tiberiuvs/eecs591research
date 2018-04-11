#!/usr/bin/env python
import uniqueid as uid
import voter

PRIVATE_KEY_LOC = 'data/sample_private_key.pem'
PUBLIC_KEY_LOC = 'data/sample_public_key.pem'
CODES_DIR = 'qrcodes'

voteMachine = voter.Voter()

for i in range(100):
    hexdump, qr = uid.generateID(PRIVATE_KEY_LOC, CODES_DIR)
    ballot = voteMachine.createBallotAuto()
    voteMachine.processBallot(ballot, hexdump)
