import math
def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False

def get_prime(number):
    while True:
        if is_prime(number):
            yield number
        number += 2

def get_sum(number):
    tmp = get_prime(3)
    summer = 2
    for i in tmp:
        if i < number:
            summer += i
        else:
            break
    return summer

if __name__ == '__main__':
    print(get_sum(2000000))
