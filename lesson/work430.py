class Clei:
    def __init__(self,*args):
        if args:
            print("传入了%d个参数，分别是：" % len(args), args)
        else:
            print("并没有传入参数")
