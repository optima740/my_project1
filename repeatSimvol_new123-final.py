def HowManyTimes(s, s_generic):
    if len(s)>len(s_generic) or (len(s)==0 or len(s_generic)==0):
        return

    s_genlist = []
    for i in range(len(s_generic)):
        s_genlist.append(s_generic[i])
    keylist = []
    for k in range(len(s)):
        keylist.append(s[k])
    k=0
    i=0
    mas_index = []
    mas_indcheck = []
    flg = 0
    while len(mas_index) != len(keylist):
        index_list = []

        for i in range (len(s_genlist)):
            if s_genlist[i] == keylist[k]:
                index_list.append(i)

        mas_index.append(index_list)

        if k<=len(keylist):

            if keylist[k] != keylist[k-1]:
                k+=1
            else:
                break


    if len(mas_index[0]) == 1 and mas_index[0] != [] and len(mas_index)== 1:
        return 1
    if len(mas_index) ==1 and len(mas_index[0]) == len(s):
        return 1
    i=0
    for i in range(len(mas_index)):
        if mas_index[i] == []:
            return


    count = 0
    mas_polozh = [0]*len(mas_index)
    i = len(mas_index)-1
    iter = 0
    while True:
        count = count + mas_index_chek(mas_polozh, mas_index)

        if i == len(mas_index)-1:
            mas_polozh[i] += 1
        else:
            i+=1
            mas_polozh[i] += 1
        if mas_polozh[i] <= len(mas_index[i])-1:
            i = len(mas_polozh)-1
            continue
        else:
            mas_polozh[i]=0
            i -=1
            if mas_polozh[i]+1 <= len(mas_index[i])-1:
                mas_polozh[i]+=1

            else:
                i -=1
        if i == -1:

            break
    return count

def mas_index_chek(mas_polozh, mas_index):
    i=0
    j=0
    k=0

    test_list = []
    for k in range (len(mas_polozh)):
        i = k
        j = mas_polozh[k]
        test_list.append(mas_index[i][j])

    return test_sort(test_list)

def test_sort(mas_test):
    count = 0
    dl = len(mas_test)
    a = mas_test[0]
    i = 0
    for i in range(len(mas_test)):
        if mas_test[i] < a:
            return 0
        elif mas_test[i] > a:
            a = mas_test[i]
    return 1

#end









