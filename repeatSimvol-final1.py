def HowManyTimes(s, s_generic):
    if len(s)>len(s_generic) or (len(s)==0 or len(s_generic)==0):
        return

    s_genlist = []
    for i in range(len(s_generic)):
        s_genlist.append(s_generic[i])
    keylist = []
    for k in range(len(s)):
        keylist.append(s[k])
    i=0
    k=0
    count_s =0
    count_key =0
    count_list = []

    while (k < len(keylist)):
        for i in range(len(s_genlist)):

            if (s_genlist[i] == keylist[k]):
                count_s +=1
            if k < len(keylist)-1:

                if (s_genlist[i] == keylist[k+1]):
                    break

        if count_s != 0:
            count_list.append(count_s)
            count_s = 0

        k+=1

    i=0
    f = 0
    rez = 1
    if len(count_list) == len(keylist):
        for i in range (len(count_list)):
            rez = (rez*count_list[i])
            f = 1


        if f != 0:
            return rez
        else:
            return

    else:
        return 0




