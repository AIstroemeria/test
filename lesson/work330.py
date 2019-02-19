def getnum(str):
    while True:
        try:
            temp = input(str)
            guess = int(temp)
            return guess
        except ValueError:
                print("请输入1到10内的数字！")
                continue
        except (EOFError, KeyboardInterrupt):
                continue

import random

secret = random.randint(1,10)
print('------------------我爱鱼C工作室------------------')
guess = getnum("不妨猜一下小甲鱼现在心里想的是哪个数字：")


    
while guess != secret:
    guess = getnum("哎呀，猜错了，请重新输入吧：")
    
    if guess == secret:
        print("我草，你是小甲鱼心里的蛔虫吗？！")
        print("哼，猜中了也没有奖励！")
    else:
        if guess > secret:
            print("哥，大了大了~~~")
        else:
            print("嘿，小了，小了~~~")
print("游戏结束，不玩啦^_^")
