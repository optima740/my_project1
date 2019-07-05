def MassVote(N, Votes):
   if N < 1 or (len(Votes)-1)< 1:
       return None

   a = Mass_Summ(Votes)
   b = Mass_Max(Votes)
   c = Votes_Procent(Votes)


   if b!=None and c!=None and c >=50 and a <= 100:
       otvet = 'majority winner'
       nomer = str(b[1]+1)
       return otvet+' '+nomer
   elif b != None and c != None and c < 50 and a <= 100:
       otvet = 'minority winner'
       nomer = str(b[1]+1)
       return otvet +' '+ nomer
   else:
       otvet = 'no winner'
       return otvet









def Votes_Procent(Votes):
    proc = 0

    if Mass_Max(Votes)!= None:
        a = Mass_Max(Votes)
                                                                # если максимум один
        proc = float((a[0]/Mass_Summ(Votes))*100)
        proc = int(proc*100)/100
        return proc
    else:
        return None                                                # случай когда максимумов несколько
def Mass_Max(Votes):
    i=0
    k=0
    max = [0]*2
    max[0] = Votes[i]
    max[1] = i
    flg = 0
    for i in range(len(Votes)):
        if Votes[i]>max[0]:
            max[0] = Votes[i]
            max[1] = i
    i=0
    for i in range(len(Votes)):
        if Votes[i] == max[0]:
            flg +=1
    if flg > 1:
        return None                     # несколько максисусов
    else:
        return max                      # один максимум


def Mass_Summ(Votes):
    i=0
    summ = 0
    for i in range(len(Votes)):
        summ = summ + Votes[i]
    return summ


