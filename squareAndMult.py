#x^c mod n
def squareMult(x, c, n):
    #Initialize
    base = x % n
    binString = intToBin(c)
    answer = 1

    if(binString[-1] == "1"):
        answer = answer * base
    binString = binString[:-1]

    #Looper
    while(binString):
        base = base**2 % n
        if (binString[-1] == "1"):
            answer = answer * base
        binString = binString[:-1]

    #Result
    answer = answer % n
    return answer

def intToBin(c):
    return "{0:b}".format(c)