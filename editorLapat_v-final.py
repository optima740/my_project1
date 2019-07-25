

#out_str = ''
out_list = []
memory_list = []
tmp_list = []
add_list = []
carent_i = [None]*1

memory_undo =[None]*1
undo_flg = [0]*1

def BastShoe(command):
    i=0
    start = 0
    ingress_list = []
    space = 0
    N = len(command)
    if command == '':
        if len(memory_list)>0:
            return memory_list[carent_i[0]]
        else:
            return None
    for i in range(N):
        if command[i] == ' ' and N > 2:
            tmp1 = command
            ingress_list.append(tmp1[start:i])
            start = i+1
            ingress_list.append(tmp1[start:N])
            space = 1

    t = command[0]
    if space == 0 and len(command)==1 and (command == '4' or command == '5'):
        ingress_list.append(command)


    elif space == 0:
        if len(memory_list)>0:
            return memory_list[carent_i[0]]
        else:
            return None

    elif space==1 and (command[0]=='4' or command[0]=='5'):
        if len(memory_list)>0:
            return memory_list[carent_i[0]]
        else:
            return None

    if len(ingress_list)>1:

        d= ingress_list[0]
        s=ingress_list[1]
    elif len(ingress_list)==1:
        d = ingress_list[0]
    elif len(ingress_list)==0:
        return None

    #print(ingress_list)
    p=int(d)
    if p == 1:
        rez = add(s)
        if undo_flg[0] == 1:
            a = memory_list[carent_i[0]]
            del memory_list[:]
            memory_list.append(a)
            memory_list.append(rez)
            undo_flg[0] = 0
            carent_i[0] = 1
        else:
            memory_list.append(rez)

        #print(memory_list)
        #print('i:',carent_i)

        return rez


    elif p == 2:

        n = int(s)
        rez = delete(n)
        if undo_flg[0] == 1:
            b = memory_list[carent_i[0]]
            del memory_list[:]
            memory_list.append(b)
            memory_list.append(rez)
            undo_flg[0] = 0
            carent_i[0] = 1
        else:
            memory_list.append(rez)

        return rez
        #print(memory_list)
        #print('i:', carent_i)



    elif p == 3:
        m = int(s)
        rez = out(m)

        return rez
    elif p == 4:
        rez = undo()

        return rez
    elif p == 5:
        rez = redo()

        return rez
    else:
        return


def add(s):

    if len(add_list) == 0:

        add_list.append(s)
        out_str = str(add_list[0])
        carent_i[0] = 0
        return out_str
    #print(out_list)
    if len(add_list)>=1:
        if len(memory_list) == 0:
            add_list.append(s)

            #carent_i[0] = len(memory_list)
            out_str = ' '.join(add_list)


            return out_str
        else:
            out_str = ''.join(memory_list[carent_i[0]]+s)
            if undo_flg[0]==0:
                carent_i[0] = len(memory_list)



            return out_str


def delete(n):

    if len(memory_list) == 0:
        return None
    #raz = len(memory_list)


    tmp_del_str = ''.join(memory_list[carent_i[0]])

    #print('del:', tmp_del_str)
    razmer = len(tmp_del_str)
    tmp_del_str = tmp_del_str[0:razmer-n]

    #carent_i[0] = len(memory_list)


    return tmp_del_str

def out(i):

    if len(memory_list) == 0 or i >= len(memory_list[carent_i[0]]):
        return None

    tmp_del_str1 = ''.join(memory_list[carent_i[0]])
    razmer = len(tmp_del_str1)
    out = str(tmp_del_str1[i])
    return out

def undo():
    undo_flg[0]=1
    if len(memory_list)== 0:
        return None
    elif len(memory_list) ==1:
        rez_undo = ''
        memory_undo[0] = 0
        return rez_undo
    elif len(memory_list) > 1:
        if carent_i[0] >= 1:

                                                                   #
            memory_undo[0] = carent_i[0]


            carent_i[0] = carent_i[0]-1
            rez_undo = str(memory_list[carent_i[0]])
            #next_i[0] = carent_i[0] + 1
            return rez_undo

        elif carent_i[0] == 0:
            rez_undo = str(memory_list[0])
            memory_undo[0] = 0
            return rez_undo

def redo():


    if memory_undo[0] == None:
        rez_redo = str(memory_list[carent_i[0]])
    else:

        rez_redo = str(memory_list[memory_undo[0]])


        if memory_undo[0] < len(memory_list)-1:
            memory_undo[0] = memory_undo[0] +1
            carent_i[0] = memory_undo[0]-1
        elif memory_undo[0] == len(memory_list)-1:

            carent_i[0] = len(memory_list)-1
        #count_i_redo[0] = razmer-1
        #carent_i[0] = next_i[0]
    return rez_redo

"""command = '1 Privet'
d = BastShoe(command)
command = '1 , Mir!'
d = BastShoe(command)
command = '1 ++'
d = BastShoe(command)
print(memory_list)
print("carent_i:", carent_i[0])
print("flg=", undo_flg)
command = '4'
d = BastShoe(command)
print(memory_list)
print("carent_i:", carent_i[0])
print("flg=", undo_flg)

command = '1 AAA'
d = BastShoe(command)

command = '4'
d = BastShoe(command)



print(d)"""






