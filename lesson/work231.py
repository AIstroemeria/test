def get_digits(n,list1 = []):
    if n:
        list1.insert(0, n % 10)
        get_digits(n // 10)
    else:
        print(list1)

n = int(input("number:"))
get_digits(n)
