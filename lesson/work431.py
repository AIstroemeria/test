class Word:
    def __init__(self,word):
        self.data = word

    def __lt__(self, other):
        tmp1 = (self.data.lstrip()).partition(' ')[0]
        tmp2 = (other.data.lstrip()).partition(' ')[0]
        return int.__lt__(len(tmp1),len(tmp2))

    def __le__(self, other):
        tmp1 = (self.data.lstrip()).partition(' ')[0]
        tmp2 = (other.data.lstrip()).partition(' ')[0]
        return int.__le__(len(tmp1),len(tmp2))

    def __eq__(self, other):
        tmp1 = (self.data.lstrip()).partition(' ')[0]
        tmp2 = (other.data.lstrip()).partition(' ')[0]
        return int.__eq__(len(tmp1),len(tmp2))

    def __ne__(self, other):
        tmp1 = (self.data.lstrip()).partition(' ')[0]
        tmp2 = (other.data.lstrip()).partition(' ')[0]
        return int.__ne__(len(tmp1),len(tmp2))

    def __gt__(self, other):
        tmp1 = (self.data.lstrip()).partition(' ')[0]
        tmp2 = (other.data.lstrip()).partition(' ')[0]
        return int.__gt__(len(tmp1),len(tmp2))

    def __ge__(self, other):
        tmp1 = (self.data.lstrip()).partition(' ')[0]
        tmp2 = (other.data.lstrip()).partition(' ')[0]
        return int.__ge__(len(tmp1),len(tmp2))
