import easygui as g
import random
import sys

while True:
    secret = random.randint(1,10)
    print("---------------------------------------")
    guess = 0
    loop = 0
    while guess != secret and loop != 3:
        temp = g.enterbox(msg='Guess a number(1~10)', title='game', default='', strip=True, image=None, root=None)
        if temp == None:
            sys.exit(0)
        while not temp.isdigit():
            g.msgbox("invalid input!")
            temp = g.enterbox(msg='Guess a number(1~10)', title='game', default='', strip=True, image=None, root=None)
        guess = int(temp)
        if guess == secret:
            g.msgbox("Right!\r\nGood job")
        else:
            if guess > secret:
                g.msgbox("Wrong!Big")
            else:
                g.msgbox("Wrong!Small")
        loop = loop + 1
        if loop == 3:
            g.msgbox("TOO MANY TIMES")
    g.msgbox("answer is " + str(secret)+'\r\nTry another time')
