for i in range(100,1000):
    tmp = 0;
    for j in str(i):
        tmp += int(j)**3
    if tmp == i:
        print(i)
