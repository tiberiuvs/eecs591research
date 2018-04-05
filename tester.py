#!/usr/bin/env python
import generate_id as gid
import validate_id as vid


for i in range(100):
    hexdump, qr = gid.generate()
    if vid.validateFromHex(hexdump):
        print('ID VALID!')
        # Now can try adding to blockchain then waiting...
    else:
        print('ID INVALID!')
