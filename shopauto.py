def ShopOLAP(N, items):
    i=0
    j=0
    if len(items)== 1:
        return items
    if len(items) == 0 or N ==0:
        return None
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
    #print(rez_list)
    sort(rez_list)
    #print(rez_list)
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

    #print(rez_list1)
    return rez_list1

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

    print(rez_list)



    while True:
        flg1 = 0
        i = 1
        while i <= (len(rez_list)-2):
            if int(rez_list[i]) == int(rez_list[i+2]):
                tmp_list = []
                a0 =  rez_list[i-1]
                a1 = rez_list[i+1]
                tmp_list.append(rez_list[i-1])
                tmp_list.append(rez_list[i+1])

                tmp_list.sort()
                if tmp_list[0] != a0 or tmp_list[1]!=a1:

                    rez_list[i+1] = tmp_list[1]

                    rez_list[i-1] = tmp_list[0]
                    flg1=1

            i+=2
        if flg1 == 0:
            break

    return rez_list


#items = ["dress1 5", "handbug32 2", "dress1 1", "handbug23 2", "handbug128 4"]
#N = 4
#d = ShopOLAP(N, items)
#print(d)