def WordSearch(len,s):
    lenM = int(round((lenstr(s)/len)))
    masstr = [[' ' for j in range(len)] for i in range(lenM)]
    iter=0

    for i in range (lenM):
        for j in range (len):
            if (iter!= lenstr(s)) :
                masstr[i][j] = s[iter]
                iter += 1

            else: break

    print(masstr, s, end='',)

def perenos(masstr, s, len, lenM):
    iter = 0
    for i in range (lenM):
        for j in range (len):
            if (j == (len-1)) and masstr[i][j] != ' ' and masstr[i+1][0] != ' ':
                masstr[i][j] = s[iter]
                iter += 1

            else: break


def lenstr(s):
    lens = 0
    for i in s:
        lens += 1
    return lens

s = 'privet mir ho ho ho'
len = 5
WordSearch(len, s)

