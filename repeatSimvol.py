def HowManyTimes(s, s_generic):
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

    while len(count_list) != len(s):
        for i in range(len(s_genlist)):
            lp = keylist[k]
            gp = s_genlist[i]
            if (s_genlist[i] == keylist[k]):
                count_s +=1
        if count_s != 0:
            count_list.append(count_s)
            count_s = 0
        k+=1
    print(count_list)
    i=0
    rez = 1
    for i in range (len(count_list)):
        rez = rez*count_list[i]

    if rez != 1:
        return rez
    else:
        return

s = '123'
s_generic = '121232343434'
d = HowManyTimes(s, s_generic)
print(d)