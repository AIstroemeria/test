def myRev(data):
    i = len(data) - 1
    while i >= 0:
        yield data[i]
        i -= 1

for i in myRev("FishC"):
    print(i, end='')
