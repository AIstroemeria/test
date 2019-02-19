import random
secret = random.randint(1,10)
print("---------------------------------------")
guess = 0
loop = 0
while guess != secret and loop != 3:
    temp = input("number:")
    while not temp.isdigit():
        print("invalid input!")
        temp = input("new number:")
    guess = int(temp)
    if guess == secret:
        print("Right!")
        print("Good job")
    else:
        if guess > secret:
            print("Wrong!Big")
        else:
            print("Wrong!Small")
    loop = loop + 1
    if loop == 3:
        print("TOO MANY TIMES")
print("answer is " + str(secret))
print("Seeyou")
