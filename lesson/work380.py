class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self):
        self.p1 = Point()
        self.p2 = Point(5,5)

    def getLen(self):
        return ((self.p1.x-self.p2.x)**2 + (self.p1.y-self.p2.y)**2)**0.5

l1 = Line()
print(l1.getLen())