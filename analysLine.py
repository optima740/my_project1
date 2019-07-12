def LineAnalysis(line):
    flg = 0
    line_item = []
    line_test = []
    for i in range(len(line)):

        if len(line) > 1 and line[0] == '*':
            flg = 1
            if i>0:
                line_item.append(line[i])
            if line[i] == '*' and i > 0:
                line_test.append(line_item)
                line_item = []
        elif len(line) == 1:
            if line[i] == "*":
                return True
            else:
                return False
        else:
            return  False
    print(line_test)
    i=0
    count = 0
    test_str = ''
    for i in range(len(line_test)):
        if i < (len(line_test)-1):
            if line_test[i]==line_test[i+1]:
                count+=1
    if count == len(line_test)-1:
        return True
    else:
        return False



    print(line_test)










line = '*..*..*..*..*..**..*'
d = LineAnalysis(line)
print(d)