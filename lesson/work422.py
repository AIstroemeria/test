class Nstr(str):
    def __add__(self,other):
        m1 = 0
        m2 = 0
        for item in self:
            m1 += ord(item)
        for item in other:
            m2 += ord(item)
        return m1 + m2

    def __sub__(self,other):
        m1 = 0
        m2 = 0
        for item in self:
            m1 += ord(item)
        for item in other:
            m2 += ord(item)
        return m1 - m2

    def __mul__(self,other):
        m1 = 0
        m2 = 0
        for item in self:
            m1 += ord(item)
        for item in other:
            m2 += ord(item)
        return m1 * m2

    def __truediv__(self,other):
        m1 = 0
        m2 = 0
        for item in self:
            m1 += ord(item)
        for item in other:
            m2 += ord(item)
        return m1 / m2

    def __floordiv__(self,other):
        m1 = 0
        m2 = 0
        for item in self:
            m1 += ord(item)
        for item in other:
            m2 += ord(item)
        return m1 // m2
