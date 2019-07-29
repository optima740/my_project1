def BiggerGreater(input):

    if len(input) == 0:
        return
    i=0
    ingress=[]
    for i in range(len(input)):
        if input[i] == ' ':
            return
        ingress.append(input[i])
    #print(ingress)
    i = len(ingress)-1

    if len(ingress) <= 1:
        rez = ''
        return rez
    elif len(ingress) == 2:
        if ingress[0]>=ingress[1]:
            rez = ''
            return rez
        elif ingress[0]<ingress[1]:
            a = ingress[0]
            ingress[0] = ingress[1]
            ingress[1] = a
            rez = ''.join(ingress)
            return rez

    i = len(ingress)-1
    k=0
    count_ravenstva = 0
    while i!=0:
        if ingress[i-1]<ingress[i]:
            i_tmp = i-1
            break

        elif ingress[i-1] == ingress[i]:
            count_ravenstva +=1
        i -= 1
    if count_ravenstva==len(ingress)-1:
        rez = ''
        return rez

    sort_ingress = []
    i = i_tmp
    while i <= len(ingress) - 1:
        sort_ingress.append(ingress[i])
        i+=1
    sort_ingress.sort()


    i=0
    while i!=len(sort_ingress):                                 #можно сделать функцию
        a = sort_ingress[i]
        if sort_ingress[i]>ingress[i_tmp]:

            tmp_sort = sort_ingress[i]
            break
        i+=1                                                    #


    i = 0

    while i!=len(ingress):
        if ingress[i] == tmp_sort:
            i_tmp2 = i
            break
        i+=1

    b = ingress[i_tmp2]
    ingress[i_tmp2] = ingress[i_tmp]
    ingress[i_tmp] = b
    #print(ingress)
    tmp_sort = []
    i=0
    if i_tmp < len(ingress)-2:
        i = i_tmp+1

        while i < len(ingress):

            tmp_sort.append(ingress[i])
            i+=1
        tmp_sort.sort()
    else:



            tmp_sort.append(ingress[i_tmp])
            tmp_sort.append(ingress[len(ingress)-1])





    #print(tmp_sort)
    a1 = ''.join(ingress)
    if i_tmp==0:

        i_tmp = i_tmp+1

    a = a1[0:i_tmp]

    b = ''.join(tmp_sort)
    rez = a+b


    #print(sort_ingress)
    #print('i_temp:',i_tmp)

    #print('i_tmp2:', i_tmp2)

    return rez


#input = 'нклм'
#d = BiggerGreater(input)
#print(d)