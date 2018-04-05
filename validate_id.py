#!/usr/bin/env python
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA
import datetime
import sys


PUBLIC_KEY_LOC = 'data/sample_public_key.pem'
TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
DELIMITER = '-'
TIMEOUT = 300


# Returns True for valid and False for invalid
def validateFromHex(message):
    # Read in the given message and split up the message
    messageList = message.split(DELIMITER)
    timestamp = bytes.fromhex(messageList[0]).decode('utf-8')
    signature = bytes.fromhex(messageList[1])
    mHash = SHA.new(timestamp.encode('utf-8'))
    # Verify the RSA signature
    publicKey = RSA.importKey(open(PUBLIC_KEY_LOC, 'r').read())
    verifier = PKCS1_PSS.new(publicKey)
    if not verifier.verify(mHash, signature):
        return False
    # Verify the message is not stale
    messageTime = datetime.datetime.strptime(timestamp, TIMESTAMP_FORMAT)
    currentTime = datetime.datetime.utcnow()
    difference = (currentTime - messageTime).seconds
    if difference > TIMEOUT:
        return False
    return True


# Returns True for valid and False for invalid
def validateFromQR(filepath):
    from qrtools.qrtools import QR
    qr = QR()
    qr.decode(filepath)
    return validateFromHex(qr.data)


if __name__ == '__main__':
    assert len(sys.argv) > 1
    validateFromHex(sys.argv[1])
