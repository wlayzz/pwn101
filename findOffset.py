from pwn import *


p = process("./pwn103.pwn103")
p.clean()
p.sendline(b"3")
p.clean()
p.sendline(cyclic(200, n=8))
p.wait()

core = p.corefile

print(cyclic_find(core.read(core.rsp, 8), n=8))