class Demo:
    def __init__(self):
        self.msg = 'FishC'

    def getmsg(self):
        return self.msg

    def setmsg(self,value):
        self.msg = value

    def delmsg(self):
        del self.msg

    x = property(getmsg,setmsg,delmsg)
