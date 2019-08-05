def TransformTransform(A, N):

    D = S(S(A))
    #print('lenD=',len(D))
    #print('S(S(A))=', D)
    Summ = sum(D)
    #print('summ=', Summ)
    if Summ%2 == 0:
        return True
    else:
        return False
def S(A):
    B_list = []
    if len(A)==1:
        B_list.append(A[0])
        return B_list
    for i in range(len(A)):
        for j in range(len(A)-i):
            k = i+j
            if j!=k:
                tmp_list = []
                p = j
                while p<=k:
                    tmp_list.append(A[p])
                    p+=1
                #print('tmp_list=',tmp_list)
                B_list.append(max(tmp_list))
            elif j==k:
                B_list.append(A[j])

    #print('len_B',len(B_list))
    #print(B_list)
    return B_list




#A = [1,2,1,7,2,4,3,1,5,1,2,1,6,1,2]
#N = len(A)
#d = TransformTransform(A,N)
#print(d)

#print(d)
