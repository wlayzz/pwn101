# Execution
`chmod +x pwn101.pwn101`
```bash
./pwn101.pwn101
       ┌┬┐┬─┐┬ ┬┬ ┬┌─┐┌─┐┬┌─┌┬┐┌─┐
        │ ├┬┘└┬┘├─┤├─┤│  ├┴┐│││├┤ 
        ┴ ┴└─ ┴ ┴ ┴┴ ┴└─┘┴ ┴┴ ┴└─┘
                 pwn 101          

Hello!, I am going to shopping.
My mom told me to buy some ingredients.
Ummm.. But I have low memory capacity, So I forgot most of them.
Anyway, she is preparing Briyani for lunch, Can you help me to buy those items :D

Type the required ingredients to make briyani: 
rice
Nah bruh, you lied me :(
She did Tomato rice instead of briyani :/
```
Après la ligne `Type the required ingredients to make briyani:` le binaire nous propose de saisir du texte.

# Analyse
## Type de fichier
```bash
file pwn101.pwn101 
pwn101.pwn101: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=dd42eee3cfdffb116dfdaa750dbe4cc8af68cf43, not stripped
```

## Checksec
```bash
checksec pwn101.pwn101 
[*] '/workspace/pwn101/pwn101.pwn101'
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      PIE enabled
```

## Ghidra
## GDB

# Pwn