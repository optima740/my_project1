def BalancedParentheses(N):
    list = [""]*2*N
    out_list=[]

    if N > 0:
        skobki(list,out_list, N, 0, 0, 0)

        return stroker(out_list, N)
def skobki(list, out_list, N, pos, open, close):

    if (close == N):
        for i in range(len(list)):
            #print(i, end="")
            out_list.append(''.join(list[i]))

        #print('-',out_list)
    else:
        if (open>close):
            list[pos] = ')'
            skobki(list,out_list, N, pos+1, open, close+1)
        if (open<N):
            list[pos] = '('
            skobki(list,out_list, N, pos + 1, open+1, close)




def stroker(list, N):
    tmp_list=[]
    tmp_str=''.join(list)
    i=0
    start = 0
    end = 0
    while i < (len(tmp_str)):
        i+=1
        end+=1
        if end == N*2:
            tmp_list.append(tmp_str[start:i])
            start = i
            end=0
    #print('LEN',len(tmp_list))
    tmp_str = ' '.join(tmp_list)
    return tmp_str

#N=3
#d = BalancedParentheses(N)
#print('end work',d)






