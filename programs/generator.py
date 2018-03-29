import datetime
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA
import qrcode


PRIVATE_KEY_LOC = 'sample_private_key.pem'
TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
DELIMITER = '0000'


def generateID(signer):
    timestamp = datetime.datetime.utcnow()
    message = timestamp.strftime(TIMESTAMP_FORMAT)
    print(message)
    mHash = SHA.new(message.encode('utf-8'))
    signature = signer.sign(mHash)
    idString = message.encode('utf-8').hex() + DELIMITER + signature.hex()
    print(idString)
    createQR(idString)


def createQR(idString):
    img = qrcode.make(idString)
    img.save('codes/{}.jpg'.format(idString[-16:]))


def startSignatureGenerator():
    privateKey = RSA.importKey(open(PRIVATE_KEY_LOC, 'r').read())
    signer = PKCS1_PSS.new(privateKey)
    print('Press enter to generate a new unique ID')
    while True:
        input()
        generateID(signer)


if __name__ == '__main__':
    startSignatureGenerator()
