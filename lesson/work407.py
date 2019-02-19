class C:
    def __init__(self, size=10):
        self.size = size

    @property
    def Size(self):
        return self.size

    @Size.setter
    def Size(self, value):
        self.size = value

    @Size.deleter
    def Size(self):
        del self.size
