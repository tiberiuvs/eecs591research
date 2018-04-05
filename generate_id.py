#!/usr/bin/env python
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA
import datetime
import qrcode


PRIVATE_KEY_LOC = 'data/sample_private_key.pem'
TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
DELIMITER = '-'
CODES_DIR = 'qrcodes'


# Returns a tuple of (hexdump, QR code filepath)
def generate():
    # Message is timestamp and its hash
    timestamp = datetime.datetime.utcnow()
    message = timestamp.strftime(TIMESTAMP_FORMAT)
    mHash = SHA.new(message.encode('utf-8'))
    # Create an RSA signature with the private key
    privateKey = RSA.importKey(open(PRIVATE_KEY_LOC, 'r').read())
    signer = PKCS1_PSS.new(privateKey)
    signature = signer.sign(mHash)
    # Create a hex value message and transform into QR code
    idString = message.encode('utf-8').hex() + DELIMITER + signature.hex()
    img = qrcode.make(idString)
    filepath = '{}/{}-{}.jpg'.format(CODES_DIR, message, idString[-16:])
    img.save(filepath)
    return (idString, filepath)


if __name__ == '__main__':
    generate()
