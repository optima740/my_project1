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
        k+=1
        mas_index.append(index_list)
    


s = '123'
s_generic = '121232343434'
d = HowManyTimes(s, s_generic)
print(d)