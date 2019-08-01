def MatrixTurn(Matrix, M, N, T):

    if M % 2 != 0 or M < 2 or N < 2:
        return

    Matrix1 = [[0 for j in range(N)] for i in range(M)]

    for i in range(M):
        stroka = Matrix[i]
        for j in range(N):
            Matrix1[i][j] = stroka[j]


    #for i in range(M):
       # print(Matrix1[i])


    while True:
        i = 0
        j = 0
        M=len(Matrix1)
        N=len(Matrix1[0])
        while True:
            tmp = Matrix1[i][j]
            border_i = i
            border_j = j
            while i < M-1:

                Matrix1[i][j] = Matrix1[i+1][j]
                i+=1

            while j < N-1:
                Matrix1[i][j] = Matrix1[i][j+1]
                j += 1
            while i > border_i:
                Matrix1[i][j] = Matrix1[i-1][j]
                i -= 1
            while j > border_j:
                Matrix1[i][j] = Matrix1[i][j-1]
                j -= 1

            Matrix1[border_i][border_j+1] = tmp

            if len(Matrix1[0])== 3 and len(Matrix1)>=4:
                i += 1
                j += 1
                a = Matrix1[i][j]
                t=1
                while i< (M/2):
                    Matrix1[i][j] = Matrix1[(M-1)-t][j]
                    Matrix1[(M-1) - t][j] = a
                    i+=1
                    t+=1
                T -= 1
                break

            elif len(Matrix1[0])>3:
                N-=1
                M-=1
                i+=1
                j+=1
                if i >= M or j >= N:
                    T -= 1
                    break
            elif len(Matrix1[0])<3:
                T -= 1
                break


        if T==0:
            break

    return(Matrix1)
    """print()
    print()
    i=0
    M=len(Matrix1)
    for i in range(M):
        print(Matrix1[i])"""










#M = 4
#N = 5
#T = 1
#Matrix = ['12345','6789a','bcdef','ghijk']
#Matrix = ['1234','5678','9abc','defg']
#Matrix = ['123','456','789','!*#']
#Matrix = ['12','34']
#d = MatrixTurn(Matrix, M, N, T)
#print(d)