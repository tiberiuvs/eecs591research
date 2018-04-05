from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA
import datetime

TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
DELIMITER = '-'
TIMEOUT = 600


# Returns a tuple of (hexdump, QR code filepath)
def generateID(privateKey, prefix):
    # Message is timestamp and its hash
    timestamp = datetime.datetime.utcnow()
    message = timestamp.strftime(TIMESTAMP_FORMAT)
    mHash = SHA.new(message.encode('utf-8'))
    # Create an RSA signature with the private key
    privateKey = RSA.importKey(open(privateKey, 'r').read())
    signer = PKCS1_PSS.new(privateKey)
    signature = signer.sign(mHash)
    # Create a hex value message and transform into QR code
    import qrcode
    idString = message.encode('utf-8').hex() + DELIMITER + signature.hex()
    img = qrcode.make(idString)
    filepath = '{}/{}-{}.jpg'.format(prefix, message, idString[-16:])
    img.save(filepath)
    return (idString, filepath)


# Returns True for valid and False for invalid
def validateIDFromHex(publicKey, message):
    # Read in the given message and split up the message
    messageList = message.split(DELIMITER)
    timestamp = bytes.fromhex(messageList[0]).decode('utf-8')
    signature = bytes.fromhex(messageList[1])
    mHash = SHA.new(timestamp.encode('utf-8'))
    # Verify the RSA signature
    publicKey = RSA.importKey(open(publicKey, 'r').read())
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
def validateIDFromQR(publicKey, filepath):
    from qrtools.qrtools import QR
    qr = QR()
    qr.decode(filepath)
    return validateIDFromHex(publicKey, qr.data)
