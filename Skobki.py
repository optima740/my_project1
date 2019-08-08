def BalancedParentheses(N):
    if N == 0:
        return None
    list = []
    count_iter=0


    skobki(list,N,count_iter)
    chek_povtor(list)
    rez = ' '.join(list)
    #print('len list=', len(list))

    return rez

def skobki(list, N,count_iter):
    tmp_list = []

    a = '('
    b = ')'

    if len(list)==0:
        list.append(a + b)
        #count_iter+=1
        N-=1
        count_iter+=1
    elif len(list)!=0:
        for i in range(len(list)):
            tmp_list.append(list[i])
        #print(tmp_list)
        list.clear()


        for i in range(len(tmp_list)):

            tmp_item = tmp_list[i]
            #stack_elem.append(tmp_item)
            list.append(tmp_item + (a+b))
            if i > 0:
                list.append((a + b)+tmp_item)

            #list.append((a+b)+tmp_item)

            list.append(a+tmp_item+b)

            if len(list)>5 and (count_iter+1)%2==0:


                e = a+(a+b)+b
                list.append(e*int((count_iter+1)/2))
        count_iter+=1
        N-=1

    if N == 0:
        #print('rez_list=', list)
        return list
    else:
        skobki(list,N,count_iter)

    #return list
def chek_povtor(list):
    i=0
    count_del=0
    while i<(len(list)):
        tmp = list[i]
        j=i
        while j<len(list):

            if i!=j:
                if tmp == list[j]:
                    del list[j]
                    count_del+=1
            j+=1
        i+=1
    """if count_del == 0:
        print('check OK')
    else:
        print('DEL elements=',count_del)"""


"""N=5
d = BalancedParentheses(N)
print(d)"""

"""mas = ['()()()','(())()','((()))()']
s = mirroring(mas)
print(s)"""