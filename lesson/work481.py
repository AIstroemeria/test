import time
class Getrun:
    def __init__(self):
        self.begin = 2000
    def __iter__(self):
        return self
    def __next__(self):
        tmp = time.localtime()[0]
        while True:
            self.begin += 4
            if self.begin % 400 == 0:
                break
            elif self.begin % 4 == 0 and self.begin % 100 != 0:
                break
        if tmp < self.begin:
            raise StopIteration
        return self.begin
