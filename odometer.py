def odometer(oksana):
    if len(oksana) >= 2:
        s = 0
        for i in range(0, len(oksana)-1, 2):
            if i < 2:
                s = oksana[i] * oksana[i+1]
            else:

                t = oksana[i+1] - oksana[i-1]
                s += oksana[i]*t
        print(s)
        return s
    else:
        return
a = [10, 2, 10, 3, 40, 6, 20, 8, 10, 9]
od = odometer(a)
