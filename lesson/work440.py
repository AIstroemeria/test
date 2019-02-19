import time as t

class MyTimer:
    def __init__(self, func = None, num = 1000000):
        self.msg = '未开始计时'
        self.begin = 0
        self.end = 0
        self.lasted = 0
        self.timer = 0
        self.func = func
        self.num = num

    def set_timer(self,ways = 1):
        if ways:
            self.timer = 1
            print('当前计时方法为:time.process_time()')
        else:
            self.timer = 0
            print('当前计时方法为:time.perf_counter()')
        

    def __add__(self,other):
        return ('总共运行了'+str(self.lasted+other.lasted)+'秒')

    def __str__(self):
        return self.msg

    __repr__=__str__

    def start(self):
        if self.timer:
             self.begin = t.process_time()
        else:
            self.begin = t.perf_counter()
        self.msg = '提示：请先调用stop()停止计时'
        print('计时开始')
        pass

    def stop(self):
        if not self.begin:
            print(self.msg)
        else:
            if self.timer:
                self.end = t.process_time()
            else:
                self.end = t.perf_counter()
            self._calc()
            print('计时结束')
    
    def _calc(self):
        self.lasted = self.end - self.begin
        self.msg = ('总共运行了'+str(self.lasted)+'秒')

    def timing(self):
        if self.func:
            for i in range(self.num):
                self.func()
            print('总共运行了'+str(t.process_time())+'秒')
