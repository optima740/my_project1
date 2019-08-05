def TransformTransform(A, N):

    D = S(S(A))
    Summ = sum(D)
    #print('summ=', Summ)
    if Summ%2 == 0:
        return True
    else:
        return False
def S(A):
    B_list = []
    for i in range(len(A)):
        for j in range(len(A)-i-1):
            k = i+j

            p = j
            tmp_list = []

            if j!=k:


                while p<k:
                    tmp_list.append(A[p])
                    p+=1
                B_list.append(max(tmp_list))
            elif j==k:

                B_list.append(A[p])

    #print('len_B',len(B_list))
    #print(B_list)
    return B_list




#A = [1,4,2,3,7,9,2,1,4,6]
#N = len(A)
#d = TransformTransform(A,N)
#d = TransformTransform(TransformTransform(A,N),L)

#print(d)
