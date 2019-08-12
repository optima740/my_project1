def Football(F,N):

    i_tmp = []
    f = check(F, i_tmp)
    if f > 2:
        tmp_list = []
        i = i_tmp[0]

        while i <= i_tmp[len(i_tmp)-1]:
            tmp_list.append(F[i])
            i+=1

        tmp_list.reverse()
        f1 = check(tmp_list, i_tmp)
        if f1 == 0:
            return True
        else:
            return False


    elif (f == 1):
        tmp = F[i_tmp[0]]
        F[i_tmp[0]] = F[i_tmp[0] + 1]
        F[i_tmp[0] + 1] = tmp
        f = check(F,i_tmp)
        if f == 0:
            return True
        else:
            return False
    elif f==2:
        replacement(F, i_tmp)

        f2 = check(F, i_tmp)
        if f2 == 0:
            return True
        else:
            return False


def replacement(F, i_tmp):

    tmp = F[i_tmp[0]]
    F[i_tmp[0]] = F[i_tmp[1]]
    F[i_tmp[1]] = tmp


def check(F, i_tmp):
    flg = 0
    i_tmp.clear()
    for i in range(len(F)-1):
        a = F[i]
        b = F[i+1]
        if F[i]>F[i+1] and flg==0:
            i_tmp.append(i)
            flg+=1
        elif F[i]>F[i+1] and flg!=0:
            i_tmp.append(i+1)
            flg+=1
    return flg


#N=9
#F = [1,9,8,2,7,6,3,5,4]
#d = Football(F, N)
#print(d)




