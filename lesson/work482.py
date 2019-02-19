class MyRev:
    def __init__(self,data):
        self.data = data
        self.i = len(self.data)
    def __iter__(self):
        return self
    def __next__(self):
        self.i -= 1
        if self.i < 0:
            raise StopIteration
        return self.data[self.i]
