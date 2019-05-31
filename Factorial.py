def squirrel(N):
    if (N >= 0):
        factor = 1
        for i in range(1, N+1):
            factor *= i
        s = str(factor)
        rez = int(s[0])
        return rez
    else:
        return




