def SynchronizingTables(N, ids, salary):

    tab = sort(ids)
    zp = sort(salary)
    hash = {}
    otvet = [0]*N
    if len(ids) != len(salary):
        return print("Faile")
    elif len(ids) and len(salary) != N:
        return print("Faile")

    for i in range (N):
        hash[tab[i]] = zp[i]
    print("Hash=", hash)
    for k in range (N):
        otvet[k] = hash[ids[k]]


    print("REZ=", otvet)

def sort(a):
    f=1
    while(f==1):
        f=0
        for i in range (len(a)-1):
            if (a[i] > a[i+1]):
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
                f=1
    return a

ids = [50, 1, 1024]
salary = [20000, 100000, 90000]
SynchronizingTables(3,ids, salary)