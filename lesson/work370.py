class Themepark():
    def __init__(self):
        self.normal = 100
        self.weekend = self.normal*1.2
        self.child = 0.5
    def get_price(self,x,y,flag):
        if flag:
            price = self.weekend
        else:
            price = self.normal
        return (x+y*self.child)*price

a = Themepark()
print(a.get_price(2,1,0))
        