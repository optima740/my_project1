def WordSearch(len,s):
    lenM = int(round((lenstr(s)/len)))
    #masstr = [[' ' for j in s] for i in s]
    liststr = []
    templist = []
    x=0
    iter = 0
    ost = len
    sim_str = 0
    for i in range (lenstr(s)):
        if ost == 0:
            if i == lenstr(s):
                liststr.append(s[x:i])

            elif s[i+1] == ' ':
                i+=1
                while s[i] == ' ':
                    i+=1
                    x=i
            else:
                liststr.append(s[x:i])
                ost = len
                x=i

        ost -=1
        sim_str +=1



        """if (i == lenstr(s)-1):
            if s[x] == ' ':
                while s[x] == ' ':
                    x+=1
                liststr.append(s[x:i])
                iter = 0
                x = i
            else:
                liststr.append(s[x:i+1])
                iter = 0
                x = i

        elif (s[i] == ' ') and (iter):
            if s[x] == ' ':
                while s[x] == ' ':
                    x+=1
                liststr.append(s[x:i])
                iter = 0
                x = i
            else:
                liststr.append(s[x:i])
                iter = 0
                x = i
        elif (iter == len-1) and s[i+1] != ' ':
            itemp = i
            liststr.append(s[x:itemp])
            x = i"""
        """while s[i] == ' ':
                i += 1
                x = i"""
        iter+=1

    for j in range(lenstr(liststr)):
        print(liststr[j])



"""def perenos(liststr, tempj, tempi, len, lenM):
    templist = []


    for tempi in range(lenM):
        for tempj in range (len):
            templist.append(liststr[tempi][tempj])

    for tempi in range(lenM):
        for tempj in range (len):
            liststr.pop([tempi][tempj])
    return templist

def vyravnivanie(liststr, s, len, lenM):
    matx = len*lenM
    razn = matx - lenstr(s)
    for i in range (razn):
        liststr.append(' ')
    print(liststr, end= ' ')"""

def lenstr(s):
    lens = 0
    for i in s:
        lens += 1
    return lens

s = '1) строка разбивается на набор строк через выравнивание по заданной ширине.'
len = 12

WordSearch(len, s)