# Execution
`chmod +x pwn102.pwn102`
```bash
./pwn102.pwn102 
       ┌┬┐┬─┐┬ ┬┬ ┬┌─┐┌─┐┬┌─┌┬┐┌─┐
        │ ├┬┘└┬┘├─┤├─┤│  ├┴┐│││├┤ 
        ┴ ┴└─ ┴ ┴ ┴┴ ┴└─┘┴ ┴┴ ┴└─┘
                 pwn 102          

I need badf00d to fee1dead
Am I right? YES
I'm feeling dead, coz you said I need bad food :(
```

# Analyse
## Type de fichier
`./pwn102.pwn102: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=2612b87a7803e0a8af101dc39d860554c652d165, not stripped`

## Checksec
```bash
checksec pwn102.pwn102 
[*] '/workspace/pwn102/pwn102.pwn102'
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      PIE enabled
```
## Ghidra
## GDB

# Pwn