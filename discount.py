def MaximumDiscount(N, price):
    #print(price)

    a = discount_all(price)

    b = summ_discount(a)
    #print('summ discount for price= ', b)
    c = discount_without(price)
    t = summ_discount(c)
    #print('summ discount for /3= ',t)
    if b > t:
        return b
    elif t > b or t == b:
        return t


def discount_without(price):                    # сортирует price по убыванию и разбивает price на price_mod по 3 вещи

    price2 = sort_price(price)
    price2.reverse()

    i = 0
    count = 0
    min = price2[i]
    tmp_mass = []
    price_mod = []
    for i in range(len(price2)):
        d = (i+1)%3
        tmp_mass.append(price2[i])
        if d == 0:

            price_mod.append(tmp_mass)
            tmp_mass = []
    #print(price_mod)
    i=0
    j=0

    dis_with = []
    for i in range(len(price_mod)):
        min = price_mod[i][j]
        for j in range(len(price_mod[i])):
            if price_mod[i][j] < min:
                min = price_mod[i][j]
        dis_with.append(min)

    #print('min in price /3= ',dis_with)
    return dis_with





def summ_discount(min_price):                           #суммарная скидка
    i=0
    summ = 0
    for i in range(len(min_price)):
        summ = summ+min_price[i]
    return summ

def discount_all(price):                                # ксидка для изачального price


    free_element = len(price) // 3

    price1 = sort_price(price)

    min_price = []

    tmp = 0

    i=0
    for i in range(free_element):
        min_price.append(price1[i])
    #print('min in price', min_price)
    return min_price

def sort_price(price):                                      # сортировка от мин к макс
    i = 0
    price1 = []
    for i in range(len(price)):
        price1.append(price[i])
    i = 0
    while True:
        count = 0
        for i in range(len(price1)):
            if i < (len(price1) - 1):
                if price1[i + 1] < price1[i]:
                    tmp = price1[i]
                    price1[i] = price1[i + 1]
                    price1[i + 1] = tmp
                    count += 1
        if count == 0:
            break
    return price1

#N = 7
#price = [100,150,200,250,300,350,400]
#d = MaximumDiscount(N, price)
#print('otvet',d)
