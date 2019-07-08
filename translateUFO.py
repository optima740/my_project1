def UFO(N, data, octal):
    if N == 0 or len(data)==0:
        return None
    elif octal == True:
        return translate_from_oct(data)
    else:
        return translate_from_hex(data)

def translate_from_oct(data):
    mas_dec_rez = []

    i=0
    for i in range(len(data)):
        mas_oct = []

        str_tmp = str(data[i])
        j =0
        for j in range(len(str_tmp)):
            mas_oct.append(int(str_tmp[j]))
        k=0
        mas_dec = []
        stepen = len(mas_oct)-1
        for k in range(len(mas_oct)):

            mas_dec.append(mas_oct[k]*(8**(stepen-k)))
        n= 0
        summ = 0

        for n in range(len(mas_dec)):
            summ = summ + mas_dec[n]

        mas_dec_rez.append(summ)
    return mas_dec_rez




def translate_from_hex(data):
    mas_dec_rez = []
    dict_symvol = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15,}
    i = 0
    for i in range(len(data)):
        mas_hex = []

        str_tmp = str(data[i])
        j = 0
        for j in range(len(str_tmp)):
            key = str_tmp[j]
            a = dict_symvol.get(key)
            if a != None:
                str_tmp.replace(key, str(a))
                mas_hex.append(a)
            else:
                mas_hex.append(int(str_tmp[j]))

        k = 0
        mas_dec = []
        stepen = len(mas_hex) - 1
        for k in range(len(mas_hex)):
            mas_dec.append(mas_hex[k] * (16 ** (stepen - k)))
        n = 0
        summ = 0

        for n in range(len(mas_dec)):
            summ = summ + mas_dec[n]

        mas_dec_rez.append(summ)
    return mas_dec_rez


#N = 3
#data = [1, 45678, 98875643]
#octal = True
#d = UFO(N, data, octal)
#print(d)
