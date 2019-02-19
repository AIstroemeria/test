tmp = input("请输入一个整数:")
inp = int(tmp)
if isinstance(inp, (int, float)) and inp >= 1:
    for i in range(inp):
        print(i+1)
    
