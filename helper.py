#Convert a string to a big integer
import binascii
def str2int(s):
    return int(binascii.hexlify(s).encode())

#Convert a big integer to a string
def int2str(i):
 h = hex(i)
 return hex2str(h)

#Helper function for int2str()
def hex2str(h):
    if len(h) > 1 and h[0:2] == '0x':
      h = h[2:]

    if h[len(h)-1] == 'L':
        h = h[0:len(h)-1]

    if len(h) % 2:
        h = "0" + h

    return binascii.unhexlify(h).decode()