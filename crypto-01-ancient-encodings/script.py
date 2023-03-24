# HTB{1n_y0ur_j0urn3y_y0u_wi1l_se3_th15_enc0d1ngs_ev3rywher3}

from Crypto.Util.number import long_to_bytes
from base64 import b64decode


def decode(c):
    c = bytes.fromhex(c[2:])  # remove 0x
    return b64decode(c)


with open("./source/output.txt", "r") as f:
    message = decode(f.readline())
    print(message)
