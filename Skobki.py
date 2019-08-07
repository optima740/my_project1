def BalancedParentheses(N):
    if N == 0:
        return None
    list = []

    skobki(list,N)
    rez = ' '.join(list)
    return rez

def skobki(list, N):

    a = '('
    b = ')'
    if len(list)==0:
        list.append(a + b)
        N-=1

    elif len(list)!=0:
        for i in range(len(list)):

            tmp_item = list[i]
            list[i] = tmp_item + (a+b)
            #tmp_item2 = tmp_item + (a+b)
            list.append(a+tmp_item+b)
        if len(list)>2:
            list.append((a+b)+tmp_item)
        N-=1
    if N == 0:
        return list
    else:
        skobki(list,N)

    #return list



#N=0
#d = BalancedParentheses(N)
#print(d)