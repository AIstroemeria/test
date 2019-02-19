class Nstr(str):
    def __sub__(self, other):
        res = ''
        for item in self:
            if item not in other:
                res = res + item
        return res

    def __lshift__(self, other):
        tmp = 2*self
        tmp = tmp[other:(other+len(self))]
        return tmp

    def __rshift__(self, other):
        tmp = 2*self
        tmp = tmp[(len(self)-other):(2*len(self)-other)]
        return tmp
