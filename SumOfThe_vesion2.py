def SumOfThe(N, data):
    if (N!=len(data)) or (N < 2):
        return print("Faile")

    sum1 = summ_array(data)
    for i in range (N):
        if (sum1 - data[i]) == data[i]:
            f = data[i]
            return data[i]

def summ_array(array):

    sum = 0
    for i in range (len(array)):
        sum = array[i]+sum
    return sum


#end