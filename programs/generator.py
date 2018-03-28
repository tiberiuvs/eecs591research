from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

# TODO: Not have it in the actual codebase...
PRIVATE_KEY = '''
MIIEowIBAAKCAQEA0oOJ80Qj+jNdqRSGRBxU98wt/XQDEm4H3hFznQmstMXIAv9A
vJnH5IZm7BA0sAmwwpIrOKiwKfpqs67G5H/FMIzFkSwwkY2Vo8YvWcSAmqKk3uUg
PNtz53XZn/7ni6b3DATbT7QbdZE0+i0lptIjgEWEjNrnUtEiP78c//9jjgcA3W6R
58q6T+X4kOrRMuvhQn6TroQzL4jBs9vsT2xheDCqzBdoTEaojlPsbDQrMOknYk9l
KZ53hxUY5uicI4n+8irOTIIfIJUdayU6lpvX+G8/N2pAfb9tkGV/D8vpvMwKlEv2
TUfkZL5gBmnRTHGARVrfWtkdyNV+I872qPcjWwIDAQABAoIBAFCtEIUmLBOK8+4E
a6BWq0l7+nQTrcm2WVWFoqUgPAvbcFeVsx2UYcL2ryLw4wBD9nXaxq2kGD8+NP4/
kQGo5c1BZcXJBaQCesKVBTiF0jNw+XZioQQxpi2iQJDMg7hFeJAmnFXjVFKuH3tx
KejQx8I04iOJEPXwKAv+FgMVwPWAjuvrQMhZYMZkgh3DNacl5GdLT/fG5bL88Z8+
kari/dZYFs062zttuqshJtJF7XK+YBo4QBdmgIbGhZL+rpijQwUo9wizMRvew1OK
AmxIr6xSCQL6Y6xmXfMLC4evvXyZXdGWSsqlKb0Ss01WpTiC4tykPxjmCqL2N4pz
W8mjs8ECgYEA/khzZaoaR0gZxD5gUWjxWUkpD2hPLEsHONQjwaArjpUbSh9EJJjk
wN+mng3mwu4an5O7PDyHU+w/cHXVBoauVFOVbzKC0z3y2LGtNgOfMLMUEqcdYI+t
6RNr7j3wNcUUAtunEfXgSL4nmcKc8WvDSTZjWr2H2SKP9Yk2OnmmYAMCgYEA0+9t
738aujf5x+4wxL/KYqgUqGgO+QLk4w6amT1+8312hdg6sgDWUzodcl/3YjhUmML0
mZ7Isl8Ik8FkdSAUlgahenuKBWbvvb/loW/Z/6bcz8y6j95PYjnv/8UlKPn5E2Rz
g77sG/l4uPkhCkm0gAsFbGz+D0UwBZm1/FkR68kCgYEAwJBhQ1Yj/GMvkBukmUId
s33h6FcXzfUrjO+p/FGtapakSeePlR9r7FvyM7NXU7s40ivwGNfFq9o22JWDMyP/
FMEPY1wfEpXROCSlhUgM37Zdtxpy9tMX4m/gxlSFelK6qsdoqANJTA0ktB5a98Ch
7OmRKABrxhWUa17zgCjrw70CgYAb6ulHaC3kI+WCYa0I7d7CGjQGbxax1KDEDDNv
RjuH5ZoMTYyF0DhrZDdmzp9uz87NBLll1xXG8V/W3t3V0/ECRkNVOBrZVVL1Yubj
2jEUTS2/Lc/Rjc5VOR6VSan4eN1Hoa7ZxvehQ76UVzTz/vuI9mqzerQI3OtTgYkI
gc8riQKBgCSwtOs229UxXDVlGqybMjJ+LaMsfgCYwcZ5/kFv2fHOlNtIXXzmKOUV
v312rF5ngRwD6Ak/fdfyuHP1X2BYzk3RLx7L03gTXIQbTooFGt3fCbTbkLFHVWnp
bjFhHxPnEQ/GkmYO0oikEnfF4r72gPymXzgCov0aiGt8rSltvX9C
'''

PUBLIC_KEY = '''AAAAB3NzaC1yc2EAAAADAQABAAABAQDSg4nzRCP6M12pFIZEHFT3zC39dAMSbgfeEXOdCay0xcgC/0C8mcfkhmbsEDSwCbDCkis4qLAp+mqzrsbkf8UwjMWRLDCRjZWjxi9ZxICaoqTe5SA823Pnddmf/ueLpvcMBNtPtBt1kTT6LSWm0iOARYSM2udS0SI/vxz//2OOBwDdbpHnyrpP5fiQ6tEy6+FCfpOuhDMviMGz2+xPbGF4MKrMF2hMRqiOU+xsNCsw6SdiT2UpnneHFRjm6Jwjif7yKs5Mgh8glR1rJTqWm9f4bz83akB9v22QZX8Py+m8zAqUS/ZNR+RkvmAGadFMcYBFWt9a2R3I1X4jzvao9yNb'''

# generate private/public key pair
key = rsa.generate_private_key(backend=default_backend(), public_exponent=65537, \
    key_size=2048)

# get public key in OpenSSH format
public_key = key.public_key().public_bytes(serialization.Encoding.OpenSSH, \
    serialization.PublicFormat.OpenSSH)

# get private key in PEM container format
pem = key.private_bytes(encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption())

# decode to printable strings
private_key_str = pem.decode('utf-8')
public_key_str = public_key.decode('utf-8')

print('Private key = ')
print(private_key_str)
print('Public key = ')
print(public_key_str)

