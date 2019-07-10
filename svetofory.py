def Unmanned(L, N, track):

    if len(track) == 0 or N == 0:
        return L
    elif track[0][1] == 0 and len(track)==1:
        return L



    i = 0
    j=0
    vremya_v_puti = 0
    koord_svetofora = 0
    pred_koord_svetofora = 0
    time_red = 0
    time_green = 0
    time = 0
    flg = 0
    koord_ostanovki = 0
    while True:
        if i == len(track):
            break
        if track[i][0] > L:
            i+=1
            continue
        koord_svetofora = track[i][0]
        time_red = track[i][1]
        time_green = track[i][2]
        time = time_red+time_green

        if i == 0:
            vremya_v_puti = koord_svetofora
            delta_svetofor = 0

        elif i!=0:
            delta_svetofor = koord_svetofora - pred_koord_svetofora
            vremya_v_puti = vremya_v_puti+delta_svetofor




        if time_red == 0:                                                                   # red not activ
            #vremya_v_puti = vremya_v_puti + delta_svetofor
            pred_koord_svetofora = koord_svetofora
        elif vremya_v_puti <= time_red:                                                     #red
            #vremya_v_puti = vremya_v_puti+delta_svetofor
            vremya_v_puti = vremya_v_puti+(time_red - vremya_v_puti)
            pred_koord_svetofora = koord_svetofora
            koord_ostanovki = koord_svetofora


        elif vremya_v_puti > time_red:
            t = vremya_v_puti//time                                                         # сколько полных циклов за время поездки
            p = vremya_v_puti - (time*t)                                                    # выделяем оставшуюся неполную часть
            d= p-time_red                                                                   # выделяем время зеленого света
            #delta_svetofor = koord_svetofora - pred_koord_svetofora
            if p < time_red :
                h = time_red - p                                                            #red
                vremya_v_puti = vremya_v_puti+h
                pred_koord_svetofora = koord_svetofora
                koord_ostanovki = koord_svetofora

            elif p == time_red or (p > time_red and d< time_green):                           #green

                #vremya_v_puti = vremya_v_puti + delta_svetofor
                pred_koord_svetofora = koord_svetofora


        i+=1

    if koord_svetofora<=L:
        tmp = L-koord_svetofora
        vremya_v_puti = vremya_v_puti+tmp

    return vremya_v_puti


#L = 10
#N = 2
#track = [[11,5,5],[15,2,2]]
#d = Unmanned(L, N, track)
#print(d)
