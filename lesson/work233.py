def getyr(n):
    if n == 1:
        return 10
    else:
        return 2 + getyr(n-1)

n = 5
print(getyr(n))
