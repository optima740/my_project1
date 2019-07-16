def ShopOLAP(N, items):
    i=0
    j=0
    if len(items)<=1 :
        return None
    if len(items)== 2:
        return items
    tmp_list = []
    for i in range(len(items)):

        for j in range(len(items[i])):
            start = 0
            if items[i][j] == ' ' and j < len(items[i])-1:
                str1 = items[i]
                tmp_list.append(str1[start:j])
                start = j+1
                tmp_list.append(str1[start:j+2])

    #print(tmp_list)
    j=0
    k=0
    i=0
    rez_list = []

    while True:
        i = 0

        key = tmp_list[0]
        rez_list.append(tmp_list[0])
        rez_list.append(tmp_list[1])
        tmp_list.pop(i)
        tmp_list.pop(i)

        while i <= len(tmp_list)-1:
            if tmp_list[i] == key:
                tmp_int= int(tmp_list[i+1])
                a = int(rez_list[k+1])
                summ = a + tmp_int
                rez_list[k+1] = summ

                tmp_list.pop(i)
                tmp_list.pop(i)

            else:
                i+=2
        k+=2

        if len(tmp_list)==0:
            break


    print(rez_list)





    sort(rez_list)
    print(rez_list)

    i = 0

    L = len(rez_list)
    rez_list1 = []
    while True:
        if i > L-2:
            break
        a = str(rez_list[i])
        b = ' '
        c= str(rez_list[i+1])

        rez_list1.append(str(a+b+c))

        i += 2


    print(rez_list1)

def sort(rez_list):

    while True:
        i = 1
        flg = 0
        while i <= (len(rez_list)-2):
            if int(rez_list[i]) < int(rez_list[i+2]):
                tmp = rez_list[i+2]
                tmp1 = rez_list[i+1]
                rez_list[i+2] = rez_list[i]
                rez_list[i+1] = rez_list[i-1]
                rez_list[i] = tmp
                rez_list[i-1] = tmp1
                flg=1
            i+=2
        if flg == 0:
            break
    return rez_list


items = ['платье1 5','сумка32 2','платье1 1','сумка23 2','сумка128 4']
N = 5
d = ShopOLAP(N, items)
print(d)