#!/usr/bin/env python
import uniqueid as uid

PRIVATE_KEY_LOC = 'data/sample_private_key.pem'
PUBLIC_KEY_LOC = 'data/sample_public_key.pem'
CODES_DIR = 'qrcodes'


for i in range(10):
    hexdump, qr = uid.generateID(PRIVATE_KEY_LOC, CODES_DIR)
    if uid.validateIDFromHex(PUBLIC_KEY_LOC, hexdump):
        print('ID VALID!')
        # Now can try adding to blockchain then waiting...
    else:
        print('ID INVALID!')
