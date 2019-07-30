def SherlockValidString(s):

    if len(s) == 0:
        return

    ingress=[]
    for i in range(len(s)):
        if s[i] == ' ':
            return
        ingress.append(s[i])
    #print(ingress)
    k=0
    i=0

    simvol_list = []
    while k<len(ingress):
        i=k
        count = 0
        a = ingress[k]
        while i < len(ingress):

            if a == ingress[i]:
                j = i
                del ingress[i]
                count+=1
                i = j
            else:
                i+=1

        simvol_list.append(count)
        k = 0
    #print(simvol_list)
    simvol_list.sort()
    #print(simvol_list)

    max = simvol_list[0]
    max_i = 0
    count = 0

    for i in range(len(simvol_list)-1):

        if simvol_list[i]<simvol_list[i+1]:
            max = simvol_list[i+1]
            max_i = i+1
        elif simvol_list[i]==simvol_list[i+1]:
            count +=1


    min = simvol_list[0]
    min_i = 0


    for i in range(len(simvol_list)-1):

        if simvol_list[i]>simvol_list[i+1]:
            min = simvol_list[i+1]
            min_i= i+1



    #print('max:', max, 'i:', max_i)
    #print('min:', min, 'i:', min_i)
    if count == len(simvol_list)-1:
        return True

    tmp = simvol_list[min_i]-1
    if tmp == 0:
        #del simvol_list[min_i]
        flg1=0
        for i in range(len(simvol_list)-1):
            if simvol_list[i] != simvol_list[i+1]:
                flg1=1
        if flg1 == 0:
            return True

    tmp = simvol_list[max_i] - 1
    simvol_list[max_i] = tmp
    flg2=0
    for i in range(len(simvol_list)-1):
        if simvol_list[i] != simvol_list[i+1]:
            flg2=1
    if flg2 == 0:
        return True
    else:
        return False


#s = 'xzxzxzza'
#d = SherlockValidString(s)
#print(d)