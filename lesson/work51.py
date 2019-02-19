tmp = input("year:")
if tmp.isdigit():
    yr = int(tmp)
    if yr % 400 == 0:
        print("yes")
    elif (yr % 4 == 0) and (yr % 100 != 0):
        print("yes")
    else:
        print("no")
    
