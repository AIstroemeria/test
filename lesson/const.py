import sys

class Const:
    def __setattr__(self, name, value):
        if not name.isupper():
            raise TypeError('常量名必须由大写字母组成！')
        if name in self.__dict__:
            raise TypeError('常量无法改变！')
        super().__setattr__(name, value)


sys.modules[__name__] = Const()
    
