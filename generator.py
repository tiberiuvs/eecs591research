#!/usr/bin/env python
import uniqueid as uid

PRIVATE_KEY_LOC = 'data/privatekey.p8'

hexdump = uid.generateID(PRIVATE_KEY_LOC)
print(hexdump)

