class MyDes:
    def __init__(self, value = 10, name = 'var'):
        self.id = name
        self.value = value

    def __get__(self, instance, owner):
        print('正在获取变量：%s' % self.id)
        return self.value

    def __set__(self, instance, value):
        print('正在修改变量：%s' % self.id)
        self.value = value

    def __delete__(self, instance):
        print('正在删除变量：%s' % self.id)
        print('噢~这个变量没法删除~')
