class Stack:
    def __init__(self):
        self.data = []

    def push(self,item):
        self.data.append(item)

    def isEmpty(self):
        if len(self.data):
            return True
        else:
            return False

    def pop(self):
        return self.data.pop()

    def top(self):
        if len(self.data):
            return self.data[-1]
        else:
            return None

    def bottom(self):
        if len(self.data):
            return self.data[0]
        else:
            return None
