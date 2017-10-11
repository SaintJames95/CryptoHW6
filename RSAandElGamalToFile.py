from RSA import RSA, enAndDecrypt
from ElGamal import ElGamal, decrypt
from helper import *

def main():
    '''
    n, p, q, b, a = RSA()
    p2, alpha, beta, a2 = ElGamal()

    keyFid = open('sheehan_keys.txt', 'w');
    keyFid.write(str(n))  # RSA n
    keyFid.write('\n')
    keyFid.write(str(b))  # RSA b
    keyFid.write('\n')
    keyFid.write(str(p2))  # ElGamal p
    keyFid.write('\n')
    keyFid.write(str(alpha))
    keyFid.write('\n')
    keyFid.write(str(beta))
    keyFid.close()

    keyFid = open('my_private_keys.txt', 'w');
    keyFid.write(str(a))  # RSA a
    keyFid.write('\n')
    keyFid.write(str(p))  # RSA p
    keyFid.write('\n')
    keyFid.write(str(q))  # RSA q
    keyFid.write('\n')
    keyFid.write(str(a2)) # El Gamal a
    keyFid.close()
    '''

    keyFid = open('sheehan_cipher.txt','r')
    yrsa = int(keyFid.readline())
    y1 = int(keyFid.readline())
    y2 = int(keyFid.readline())
    keyFid.close()

    keyFid = open('sheehan_keys.txt', 'r')
    n = int(keyFid.readline())
    x = int(keyFid.readline())
    p = int(keyFid.readline())
    keyFid.close()

    keyFid = open('my_private_keys.txt', 'r')
    rsaA = int(keyFid.readline())
    x = int(keyFid.readline()) #Ignore
    x = int(keyFid.readline()) #Ignore
    elA = int(keyFid.readline())
    keyFid.close()

    rsaMessage = (enAndDecrypt(yrsa, rsaA, n))
    elMessage = (decrypt(y1,y2,p,elA))

    Rstr = int2str(rsaMessage)
    Estr = int2str(elMessage)
    print(Rstr)
    print(Estr)

    keyFid = open('sheehan_text.txt', 'w');
    keyFid.write(Rstr)  # RSA string
    keyFid.write('\n')
    keyFid.write(Estr)  # ElGamal string
    keyFid.close()

if __name__ == "__main__":
    main()
