class Nint(int):
    def __new__(cls, strr):
        if isinstance(strr, str):
            res = 0
            for item in strr:
                res += ord(item)
            return res
        else:
            return int.__new__(cls, strr)
