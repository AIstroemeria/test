import random
import time

class Turtle:
    def __init__(self):
        self.hp = 100
        self.x = random.randint(1,10)
        self.y = random.randint(1,10)
    
    def move(self):
        pace = random.randint(1,2)
        dirction = random.randint(1,4)
        if dirction == 1:
            self.x += pace
        elif dirction == 2:
            self.x -= pace
        elif dirction == 3:
            self.y += pace
        elif dirction == 4:
            self.y -= pace

        if self.x > 10:
            self.x = 20 - self.x
        elif self.x < 0:
            self.x = -self.x
        if self.y > 10:
            self.y = 20 - self.y
        elif self.y < 0:
            self.y = -self.y
        
        self.hp -= 1
        if self.hp <= 0:
            return False
        else:
            return True
    
    def eat(self):
        self.hp += 20
        if self.hp > 100:
            self.hp = 100

class Fish:
    def __init__(self):
        self.x = random.randint(1,10)
        self.y = random.randint(1,10)
    
    def move(self):
        pace = 1
        dirction = random.randint(1,4)
        if dirction == 1:
            self.x += pace
        elif dirction == 2:
            self.x -= pace
        elif dirction == 3:
            self.y += pace
        elif dirction == 4:
            self.y -= pace

        if self.x > 10:
            self.x = 20 - self.x
        elif self.x < 0:
            self.x = -self.x
        if self.y > 10:
            self.y = 20 - self.y
        elif self.y < 0:
            self.y = -self.y

def print_pos(t,fishes):
    temp = ['*'*11 for i in range(11)]
    temp[t.x] = temp[t.x][0:t.y] + 'T' + temp[t.x][(t.y+1):11]
    for item in fishes:
        if temp[item.x][item.y] == 'T':
            temp[item.x] = temp[item.x][0:item.y] + 'M' + temp[item.x][(item.y+1):11]
        else:
            temp[item.x] = temp[item.x][0:item.y] + 'f' + temp[item.x][(item.y+1):11]
    for ss in temp:
        print(ss)

t = Turtle()
fishes = [Fish() for i in range(10)]   
counts = 0
log = ''
while True:
    print_pos(t,fishes)
    print("第%d次 剩余体力：%d" % (counts,t.hp))
    counts += 1
    print(log)
    res = t.move()
    get = -1
    for i in range(len(fishes)):
        fishes[i].move()
        if fishes[i].x == t.x and fishes[i].y == t.y:
            get = i
    if get != -1:
        log = log + ('第%d条小鱼被吃了...' % get)
        t.eat()
        del fishes[get]
    
    if res == False or fishes == []:
        break
    time.sleep(0.5)

print_pos(t,fishes)
print("第%d次 剩余体力：%d" % (counts,t.hp))
print('游戏结束')
if fishes == []:
    input("小鱼全被吃掉了")
else:
    input("体力耗尽！")