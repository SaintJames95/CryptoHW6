def multInvByForce(a,m):
    b = 0
    while True:
        b += 1
        if ((a * b) % m == 1):
            return b