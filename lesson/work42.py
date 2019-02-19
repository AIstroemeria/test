tmp = input("请输入一个整数：")
inp = int(tmp)
if isinstance(inp,int):
    for i in range(inp):
        i = 8 - i
        print((i-1)*' '+i*'*')
        
