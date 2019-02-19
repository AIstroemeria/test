import pickle
import os

class MyDes:
    def __init__(self, name = 'name', value = None):
        self.id = name
        self.value = value
        with open(name+'.pkl', 'wb') as pf:
            pickle.dump(self.value, pf)

    def __get__(self, instance, owner):
        with open(self.id+'.pkl', 'rb') as pf:
            tmp = pickle.load(pf)
        return tmp

    def __set__(self, instance, value):
        self.value = value
        with open(self.id+'.pkl', 'wb') as pf:
            pickle.dump(self.value, pf)

    def __delete__(self, instance):
        os.remove(self.id+'.pkl')
