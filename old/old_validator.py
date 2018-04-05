import datetime
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA


PUBLIC_KEY_LOC = 'sample_public_key.pem'
TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
DELIMITER = '0000'


def verifyID(verifier, fullMessage):
    messageList = fullMessage.split(DELIMITER)
    timestamp = bytes.fromhex(messageList[0]).decode('utf-8')
    signature = bytes.fromhex(messageList[1])
    mHash = SHA.new(timestamp.encode('utf-8'))
    if not verifier.verify(mHash, signature):
        print('SIGNATURE INVALID')
        return False
    messageTime = datetime.datetime.strptime(timestamp, TIMESTAMP_FORMAT)
    currentTime = datetime.datetime.utcnow()
    difference = (currentTime - messageTime).seconds
    if difference > 300:
        print('TIMESTAMP TOO OLD')
        return False


def startSignatureVerifier():
    publicKey = RSA.importKey(open(PUBLIC_KEY_LOC, 'r').read())
    verifier = PKCS1_PSS.new(publicKey)
    while True:
        message = input()
        verifyID(verifier, message)


if __name__ == '__main__':
    startSignatureVerifier()
