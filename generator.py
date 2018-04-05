#!/usr/bin/env python
import uniqueid as uid

PRIVATE_KEY_LOC = 'data/sample_private_key.pem'
CODES_DIR = 'qrcodes'

hexdump, qr = uid.generateID(PRIVATE_KEY_LOC, CODES_DIR)
print(hexdump)
print(qr)
