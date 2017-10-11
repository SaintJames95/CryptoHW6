from RSA import randomXbitPrime
from RSA import millerRabinTenTimes
from squareAndMult import squareMult
from eea2 import modinv
import random

def ElGamal():
    q = None
    p = None
    condition = False
    while not condition:
        q = randomXbitPrime(255)
        p = 2*q + 1
        condition = millerRabinTenTimes(p)

    #Private Key
    a = random.randint(2, p - 2)

    #Public Key
    alpha = randomPrimitiveRoot(p, q, 2)
    beta = squareMult(alpha, a, p)

    return p, alpha, beta, a

    #Test
    #Choose Random K <= p-2
    #k = random.randint(2, p - 2)
    #Actual Message
    #y1, y2 = encrypt(x, k, p, alpha, beta)
    #dText = decrypt(y1, y2, p ,a)

def encrypt(x, k, p, alpha, beta):
    y1 = squareMult(alpha, k, p)
    y2 = (squareMult(beta,k,p)*x) % p
    return y1, y2

def decrypt(y1, y2, p, a):
    return y2*(modinv(squareMult(y1, a, p), p)) % p

def randomPrimitiveRoot(p, factor1, factor2):
    alpha = None
    condition = False
    while not condition:
        alpha = random.randint(2, p - 1)
        exp1 = (p - 1) // factor1
        exp2 = (p - 1) // factor2
        condition = (squareMult(alpha, exp1, p) != 1) \
                    and (squareMult(alpha, exp2, p) !=1)
    return alpha