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
    while len(mas_index) != len(keylist):
        index_list = []
        for i in range (len(s_genlist)):
            if s_genlist[i] == keylist[k]:
                index_list.append(i)

        mas_index.append(index_list)
        k += 1
    print(mas_index)


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




    print(count)








def mas_index_chek(mas_polozh, mas_index):
    i=0
    j=0
    k=0

    test_list = []
    for k in range (len(mas_polozh)):
        i = k
        j = mas_polozh[k]
        test_list.append(mas_index[i][j])
        print("test_list=", test_list)
    return test_sort(test_list)



"""
def iter_list_for_chek(mas_polozh):
    i =0

    mas_polozh1 = []
    for i in range(len(mas_polozh)):
        if mas_polozh1[i]+1 >= mas_polozh[i]:
            break
        else:
            mas_polozh1[i]+1
            

        print(mas_polozh1)

"""



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










s = '123'
s_generic = '1102353'
d = HowManyTimes(s, s_generic)
print(d)
"""
mas_t = [0, 1, 4]
d = test_sort(mas_t)
print(d)"""



