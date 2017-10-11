from millerRabin import millerRabin
from squareAndMult import squareMult
from eea2 import modinv
import math
import random

def RSA():

    #Size of p and q in bits
    x = 512
    p = randomXbitPrime(x)
    q = randomXbitPrime(x)

    phi = (p-1)*(q-1)

    #PUBLIC KEY:
    n = p * q
    b = random.randint(2, phi - 1)
    #While not relatively prime
    while math.gcd(b,phi) != 1 or math.gcd(b,n) != 1:
        b = random.randint(2, phi - 1)

    #PRIVATE KEY
    a = modinv(b, phi)

    #TEST
    #text = 54761234675
    #eText = enAndDecrypt(text, b, n)
    #dText = enAndDecrypt(eText, a, n)

    return n, p, q, b, a

def enAndDecrypt(text, exp, n):
    return squareMult(text, exp, n)

def randomXbitPrime(x):
    p = None
    condition = False
    while not condition:
        p = random.getrandbits(x)
        if (p % 2 == 0):
            p -= 1
        condition = millerRabinTenTimes(p)
    return p

def millerRabinTenTimes(n):
    for x in range(10):
        if not millerRabin(n):
            return False
    return True

