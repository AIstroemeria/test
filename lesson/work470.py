class CountList:
    def __init__(self, *args):
        self.values = [x for x in args]
        self.count = [0 for x in args]

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        self.count[key] += 1
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value
        self.count[key] = 0

    def __delitem__(self, key):
        del self.values[key]
        del self.count[key]

    def counter(self, index):
        return self.count[index]

    def append(self, item):
        self.values.append(item)
        self.count.append(0)

    def pop(self):
        key = len(self.values) - 1
        tmp = self.values[key]
        del self.values[key]
        del self.count[key]
        return tmp

    def remove(self, key):
        del self.values[key]
        del self.count[key]

    def insert(self, key, item):
        self.values.insert(key, item)
        self.count.insert(key, 0)

    def clear(self):
        for key in range(len(self.values)):
            del self.values[0]
            del self.count[0]

    def reverse(self):
        self.values.reverse()
        self.count.reverse()
