def SumOfThe(N, data):
    if (N!=len(data)) or (N < 2):
        return

    sum1 = summ_array(data)
    for i in range (N-1):
        if (sum1 - data[i]) == data[i]:
            return data[i]

def summ_array(array):

    sum = 0
    for i in range (len(array)):
        sum = array[i]+sum
    return sum


