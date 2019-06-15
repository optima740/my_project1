def WordSearch(len,s, subs):

    liststr = []

    x=0
    space = 0
    ost = len
    i_space = 0

    for i in range (lenstr(s)):

        if (s[i] == ' '):
            space = i
            i_space +=1
        if (ost == 0) and (i<(lenstr(s)-1)) and (s[i] != ' '):
            if (i_space != 0):
                liststr.append(s[x:space])
                delta = i - space
                x = space+1
                i_space = 0
                ost = len - (delta-1)

            elif (i_space == 0):
                liststr.append(s[x:i])
                x = i+1
                ost = len

        elif (ost == 0) and (i<(lenstr(s)-1)) and (s[i] == ' '):
            liststr.append(s[x:i])
            x = i+1
            ost = len
        elif (i == (lenstr(s)-1)):
            liststr.append(s[x:i+1])
        ost -=1

    nomer_str = None
    for i in range (lenstr(liststr)):

        temp_str = liststr[i]
        x1 = 0

        for t in range (lenstr(temp_str)):

            if (temp_str[t] == ' ') or (temp_str[t] == '.') or (temp_str[t] == ',') or (temp_str[t] == '!'):

                srez = temp_str[x1:t]
                if (srez == subs):

                    nomer_str = i
                x1 = t + 1

            if (t == lenstr(temp_str)-1):
                srez = temp_str[x1:t + 1]
                if (srez == subs):

                    nomer_str = i

                x1= t+1

    rez = [0]*lenstr(liststr)
    if nomer_str != None:

        rez[nomer_str] = 1
        return rez
    else:
        return rez


def lenstr(s):
    lens = 0
    for i in s:
        lens += 1
    return lens



