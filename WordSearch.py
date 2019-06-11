def WordSearch(len,s):
    lenM = int(round((lenstr(s)/len)))
    masstr = [[' ' for j in range(lenM)] for i in range(len)]
    iter=0

    for i in range (len):
        for j in range (lenM):
            if iter!= lenstr(s):

                masstr[i][j] = s[iter]
                iter += 1
            else: break

    print(masstr, s, end='',)


def lenstr(s):
    lens = 0
    for i in s:
        lens += 1
    return lens

s = 'privet mir ho ho ho'
len = 5
WordSearch(len, s)

