#!/usr/bin/env python3

from pwn import *
from pwn import p64


host = "165.22.116.7:31560"


if args.REMOTE:
    ip, port = host.split(":")
    p = remote(ip, port)
else:
    p = process("./license")

payload = b"A" * (0x20 + 8)
payload += p64(0x401176)

# Start exam

p.recvuntil(b"(y/n)\n")
p.sendline(b"y")

# First password

p.recvuntil(b"This one's not even hidden: ")

password_first = b"PasswordNumeroUno"

p.sendline(password_first)
print(p.recvline().decode()[:-1])

# Second password

p.recvuntil(b"what\'s the second password? ")

password_second = b'\x30\x77\x54\x64\x72\x30\x77\x73\x73\x34\x50'
print(password_second.decode())
password_second = password_second[::-1]  # reverse

p.sendline(password_second)
print(p.recvline().decode()[:-1])

# Third password

p.recvuntil(b"give me the third, and most protected, password: ")

password_third_xor = b'\x47\x7b\x7a\x61\x77\x52\x7d\x77\x55\x7a\x7d\x72\x7f\x32\x32\x32\x13'
password_third = [""] * len(password_third_xor)

for i in range(len(password_third)):
    password_third[i] = chr(password_third_xor[i] ^ 0x13)

password_third = "".join(password_third).encode()

p.sendline(password_third)
print(p.recvline().decode()[:-1])

# Final output

print(p.recvall().decode()[:-1])
