for i in range(100,1000):
    temp = [int(x)**3 for x in (list(str(i)))]
    if sum(temp) == i:
        print(i)
