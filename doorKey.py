def Keymaker(k):

    doors = [True]*k
    i=0
    n=1
    step=1
    while n<=k:
        i = step
        while i<len(doors):
            a = doors[step]
            doors[i] = not(doors[i])
            i+=1
            i+=step
        step+=1
        n+=1
    #print(doors)
    #print('Doors=',counter_doors(doors))
    rez = out_rez(doors)
    #print('Modify:',doors)
    #print(rez)
    return rez
def out_rez(doors):
    for i in range(len(doors)):
        if doors[i] == True:
            doors[i] = '1'
        else:
            doors[i]='0'
    rez = ''.join(doors)
    return rez
def counter_doors(doors):
    count=0
    for i in range(len(doors)):
        if doors[i] == True:
            count+=1
    return count

#d = Keymaker(1)

#print(d)