import random
from squareAndMult import squareMult

#Return True For Prime, False for composite.
def millerRabin(p):
    #If Even Not Prime
    if p % 2 == 0:
        return False

    n = p - 1
    k = 0

    m = n
    #Find Exponent (k) of a
    while(m % 2 == 0):
        m = m // 2
        k+=1

    m = int(m)
    # Random a between 1 and n (2 and n-1 inclusive)
    a = random.randint(2, (n-1))
    # Square and Multiply for B0
    b = squareMult(a,m,p)

    if b == 1:
        return True
    else:
        for x in range(k):
            # n is p - 1
            if b == -1 or b == n:
                return True
            else:
                b = (b**2) % p

        return False