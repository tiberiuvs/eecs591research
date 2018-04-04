#!/usr/bin/env python
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA
import datetime
import qrcode
from qrtools.qrtools import QR
import sys


PUBLIC_KEY_LOC = 'sample_public_key.pem'
TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
DELIMITER = '0000'
TIMEOUT = 300


assert len(sys.argv) > 1
# Read in the given QR code and split up the message
filepath = sys.argv[1]
qr = QR()
qr.decode(filepath)
messageList = qr.data.split(DELIMITER)
timestamp = bytes.fromhex(messageList[0]).decode('utf-8')
signature = bytes.fromhex(messageList[1])
mHash = SHA.new(timestamp.encode('utf-8'))
# Verify the RSA signature
publicKey = RSA.importKey(open(PUBLIC_KEY_LOC, 'r').read())
verifier = PKCS1_PSS.new(publicKey)
if not verifier.verify(mHash, signature):
    print('ININVALID')
    sys.exit()
# Verify the message is not stale
messageTime = datetime.datetime.strptime(timestamp, TIMESTAMP_FORMAT)
currentTime = datetime.datetime.utcnow()
difference = (currentTime - messageTime).seconds
if difference > TIMEOUT:
    print('STALE')
    sys.exit()
print('VALID')
