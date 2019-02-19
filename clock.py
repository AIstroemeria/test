# -*- coding: UTF-8 -*-
from tkinter import *
top = Tk()

li = ['a','b','c']
lb = ['A','B','C']
listi = Listbox(top)
listb = Listbox(top)
for item in li:
    listi.insert(0,item)
for item in lb:
    listb.insert(0,item)

listi.pack()
listb.pack()
top.mainloop()