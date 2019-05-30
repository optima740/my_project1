import math


def squirrel(n):
    if (n >= 0):
        s = str(math.factorial(n))
        #print(s)
        rez = int(s[0])
        print(rez)
    else:
        return print("Faile")




squirrel(0)