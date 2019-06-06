def ConquestCampaign(N, M, L, battalion):

    oblast = [[0 for j in range(M)] for i in range(N)]

    for i in range(len(battalion)):
        if (len(battalion)< L*2):
            return
        elif (i % 2 == 0):

            if (battalion[i] > N):
                return
        else:
            if (battalion[i] > M):
                return
    t =0
    tmp = [0]*2
    for i in range (L*2):
        tmp[t] = battalion[i]
        t += 1
        if t == 2:
            oblast[tmp[0]-1][tmp[1]-1] = 1
            t = 0
    day = 0
    f = 0
    while (f==0):
        f = 1
        for i in range (N):
            for j in range (M):

                if oblast[i][j] != 0 :
                    oblast[i][j] += 1
        day +=1

        for i in range(N):
            for j in range(M):
                if oblast[i][j] == 0:
                    f = 0


                    if (i == 0 and j == 0) and ((oblast[i][j+1] >= oblast[i][j] +2) or (oblast[i+1][j] >= oblast[i][j]+2)): # левый верхний угол
                        oblast[i][j] += 1


                    elif (i== 0 and j == M-1) and ((oblast[i][j-1]>=oblast[i][j]+2) or (oblast[i+1][j]>=oblast[i][j]+2)): # правый верхний угол
                        oblast[i][j] += 1


                    elif (i == N-1 and j == M-1) and ((oblast[i-1][j]>=oblast[i][j]+2) or (oblast[i][j-1]>=oblast[i][j]+2)): # правый нижний угол
                        oblast[i][j] += 1


                    elif (i == N-1 and j == 0) and ((oblast[i-1][j]>=oblast[i][j]+2) or (oblast[i][j+1]>=oblast[i][j]+2)): # левый нижний угол
                        oblast[i][j] += 1

                    elif (i > 0 and i < N-1 and j == 0) and ((oblast[i-1][j]>=oblast[i][j]+2) or (oblast[i][j + 1]>=oblast[i][j]+2) or (oblast[i+1][j]>=oblast[i][j]+2)): # левая вертикаль
                        oblast[i][j] += 1

                    elif (j > 0 and j < M-1 and i == 0) and ((oblast[i][j-1]>=oblast[i][j]+2) or (oblast[i][j + 1]>=oblast[i][j]+2) or (oblast[i+1][j]>=oblast[i][j]+2)): # верхняя горизонталь
                        oblast[i][j] += 1

                    elif (i > 0 and i < N-1 and j == M-1) and ((oblast[i-1][j]>=oblast[i][j]+2) or(oblast[i][j - 1]>=oblast[i][j]+2) or (oblast[i+1][j]>=oblast[i][j]+2)): # левая вертикаль
                        oblast[i][j] += 1
                    elif (j > 0 and j < M-1 and i == N-1) and ((oblast[i][j+1]) or (oblast[i][j - 1]) or (oblast[i-1][j])): # нижняя горизонталь
                        oblast[i][j] += 1
                    elif  ((j > 0 and j < M-1 and i > 0 and i < N-1)) and ((oblast[i+1][j] >=oblast[i][j]+2) or (oblast[i-1][j]>=oblast[i][j]+2) or (oblast[i][j+1]>=oblast[i][j]+2) or (oblast[i][j-1])):
                        oblast[i][j] += 1

    return day



