def SumOfThe(N, data):
    if (N!=len(data)) or (N < 2):
        return
    a=0
    i=0

    for i in range(N):
        temp_list = []
        a = i
        j=0
        while j != (N):

            if a != j:

                temp_list.append(data[j])
                #s = temp_list[j]
                j+=1
            else:
                j+=1


        if summ_array(temp_list) == data[a]:
            rez = data[a]
            return rez

def summ_array(array):
    sum = 0
    for i in range (len(array)):
        sum = array[i]+sum
    return sum

