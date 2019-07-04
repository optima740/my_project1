def BigMinus(s1,s2):

    s1_list = []
    s2_list = []
    i=0
    j=0
    if len(s1)>1 and len(s2)>1:
        while s1[i] == '0':
            i+=1
        while s2[j] == '0':
            j+=1
        s11 = s1[i:len(s1)]
        s22 = s2[j:len(s2)]
    else:
        s11 = s1
        s22 = s2



    j=0
    if len(s11)>len(s22):
        i = 0
        for i in range(len(s11)):
            s1_list.append(int(s11[i]))
        i=0
        for i in range(len(s22)):
            s2_list.append(int(s22[i]))
    elif len(s11)<len(s22):
        i=0
        for i in range(len(s11)):
            s2_list.append(int(s11[i]))
        i=0
        for i in range(len(s22)):
            s1_list.append(int(s22[i]))
    else:
        i=0
        flg = 0
        for i in range(len(s11)):
            if int(s11[i]) > int(s22[i]) and int(s22[i]) < int(s11[i]):
                flg = 1
                break
            elif int(s11[i]) < int(s22[i]) and int(s22[i]) > int(s11[i]):
                break
        if flg !=0:
            i = 0
            for i in range(len(s11)):
                s1_list.append(int(s11[i]))
            i = 0
            for i in range(len(s22)):
                s2_list.append(int(s22[i]))
        else:
            i = 0
            for i in range(len(s11)):
                s2_list.append(int(s11[i]))
            i = 0
            for i in range(len(s22)):
                s1_list.append(int(s22[i]))

    len_s1 = len(s1_list)
    len_s2 = len(s2_list)




    index = 0
    list_rez = []
    i=len_s1 -1
    j=len_s2 -1
    while True:
        if len_s1 == len_s2 == 1:
            list_rez.append(s1_list[i] - s2_list[j])
            break

        if s1_list[i] >= s2_list[j]:

            list_rez.append(s1_list[i] - s2_list[j])
            i-=1
            j-=1

        else:

            i-=1
            if s1_list[i] != 0 :
                s1_list[i] = s1_list[i]-1
                i+=1
                list_rez.append((s1_list[i]+10) - (s2_list[j]))

                i-=1
                j-=1
            elif s1_list[i] ==0 :
                index = i
                while s1_list[i]==0: #or i > -1:
                    a = s1_list[i]
                    s1_list[i] = 9
                    i -= 1

                s1_list[i] = s1_list[i] - 1
                i = index
                s1_list[i+1] = s1_list[i+1] +10
                list_rez.append(s1_list[i+1]-s2_list[j])
                j-=1
        if j == -1:
            while True:
                if i==-1:
                    break
                list_rez.append(s1_list[i])
                i-=1

        if i == -1:
            break
    list_rez1 =[]
    i=len(list_rez) -1
    while True:
        if i==-1:
            break
        if len(list_rez)==1:
            list_rez1.append(list_rez[i])
            break
        else:
            list_rez1.append(list_rez[i])
            i-=1
    i=0
    while True and len(list_rez1)>1:
        if list_rez1[i] == 0:
            list_rez1.pop(i)

        else:
            break






    i = 0
    return ''.join([str(i) for i in list_rez1])





