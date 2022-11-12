self_num_list = []
tmp = []

for _ in range(10000):
    self_num_list.append(0)      

for i in range(1,10000):
    
    if len(str(i)) == 1:
        self_num_list[i+i] = 1

    elif len(str(i)) == 2:
        tmp.append(str(i)[0])
        tmp.append(str(i)[1])
        self_num_list[int(tmp[0])+int(tmp[1])+i] = 1

    elif len(str(i)) == 3:
        tmp.append(str(i)[0])
        tmp.append(str(i)[1])
        tmp.append(str(i)[2])
        self_num_list[int(tmp[0])+int(tmp[1])+int(tmp[2])+i] = 1

    elif len(str(i)) == 4:
        try:
            tmp.append(str(i)[0])
            tmp.append(str(i)[1])
            tmp.append(str(i)[2])
            tmp.append(str(i)[3])
            self_num_list[int(tmp[0])+int(tmp[1])+int(tmp[2])+int(tmp[3])+i] = 1  
        except:
            pass
    tmp.clear()

for i in range(1,10000):
    if self_num_list[i] == 0:
        print(i)