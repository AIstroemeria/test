import time as t
class Record:
    def __init__(self, value = 10, name = 'name'):
        self.id = name
        self.value = value

    def __get__(self, instance, owner):
        with open('record.txt', 'a') as f:
            msg = '读取变量%s  ' % self.id
            tmp = t.localtime()[:6]
            form = ['年','月','日 ',':',':','']
            for i in range(6):
                msg = msg + str(tmp[i]) + form[i]
            f.write('\n')
            f.write(msg)

        return self.value

    def __set__(self, instance, value):
        with open('record.txt', 'a') as f:
            msg = '更改变量%s为%s  ' % (self.id,str(value))
            tmp = t.localtime()[:6]
            form = ['年','月','日 ',':',':','']
            for i in range(6):
                msg = msg + str(tmp[i]) + form[i]
            f.write('\n')
            f.write(msg)

        self.value = value
