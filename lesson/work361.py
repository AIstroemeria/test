class Rectangle():
    longth = 10
    width = 5
    
    def setRect(self):
        print("please insert longth and width.")
        self.longth = float(input("longth:"))
        self.width = float(input("width:"))
    
    def getRect(self):
        print("the longth is %f and width is %f" % (self.longth,self.width))
    
    def getArea(self):
        print(self.longth * self.width)