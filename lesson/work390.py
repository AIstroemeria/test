class Test:
    num = 0
    def __init__(self):
        Test.num += 1

a = Test()
b = Test()
c = Test()
print(Test.num)
