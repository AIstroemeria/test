import os
import sys
import easygui as g
from tkinter import *  #控件基础包，导入这个包后，这个包下的所有函数可以直接调用
from tkinter import ttk
import time
import threading

#跟踪目标文件，显示上一句文本
def change_curchap(*args):
    global flag
    if not os.path.isdir(os.path.join(os.getcwd(),curchap.get())):
        flag = 0
        msg = '未发现此目录!'
        lastsub.delete(1.0, END)
        lastsub.insert(END, msg)
    else:
        flag = 1
        filepath = os.path.join(workpath, curchap.get())
        filepath = os.path.join(filepath, '%s.txt' % comboxlist1.get())
        if not os.path.exists(filepath):
            with open(filepath, 'w') as f:
                msg = '[空]'
                pass
        else:
            with open(filepath, 'r') as f:
                msg = f.read()
                if msg == '':
                    msg = '[空]'
        lastsub.config(state = NORMAL)
        lastsub.delete(1.0, END)
        lastsub.insert(END, msg)
        lastsub.see(END)
        lastsub.config(state = DISABLED)

def delsub(*args):
    global flag
    if not flag:
        if g.boolbox('目标文件不存在，是否创建？', 'warning!'):
            os.mkdir(curchap.get())
            flag = 1
        else:
            return
    filepath = os.path.join(workpath, curchap.get())
    filepath = os.path.join(filepath, '%s.txt' % comboxlist1.get())
    with open(filepath, 'r') as f:
        cursub = f.readlines()
    if len(cursub):
        del cursub[-1]
        with open(filepath, 'w') as f:
            f.writelines(cursub)
        change_curchap()

def insertsub(*args):
    global flag
    if not flag:
        if g.boolbox('目标文件不存在，是否创建？', 'warning!'):
            os.mkdir(curchap.get())
            flag = 1
        else:
            return
    filepath = os.path.join(workpath, curchap.get())
    filepath = os.path.join(filepath, '%s.txt' % comboxlist1.get())
    with open(filepath, 'a') as f:
        tmp = textinsert.get(1.0, END)
        f.write(tmp.replace('\n','')+'\n')
    textinsert.delete(1.0, END)
    change_curchap()

if __name__ == '__main__':
    workpath = r'C:\Users\hn810\Desktop\イロドリミドリ'
    os.chdir(workpath)

    flag = 0
    win=Tk() #构造窗体
    win.geometry('600x250')
    win.title("add subtitles")

    Label(win, text='chap:').grid(row=0, column=0, sticky=W)
    curchap = StringVar()
    curchap.trace('w', change_curchap)
    e1 = Entry(win, textvariable=curchap) #初始化
    e1.grid(row=0, column=1, columnspan=2, sticky=W+E)

    Label(win, text='chara:').grid(row=1, column=0, sticky=W)
    comboxlist1=ttk.Combobox(win) #初始化
    comboxlist1['values']=('緒形アリシアナ','天王洲なずな','小仏凪','箱部なる','明坂芹菜')
    comboxlist1.current(0)
    comboxlist1.bind("<<ComboboxSelected>>",change_curchap)  #绑定事件,(下拉列表框被选中时，绑定go()函数)
    comboxlist1.grid(row=1, column=1, columnspan=2, sticky=W+E)

    Label(win, text='插入:').grid(row=2, column=0, sticky = W)
    textinsert = Text(win, height = 1, width=40)
    textinsert.grid(row=2, column=1,columnspan=6,sticky = W+E)
    textinsert.bind('<Key-Return>', insertsub)

    lastsub = Text(win, height = 10, state = DISABLED)
    lastsub.grid(row=3, column=0,columnspan=6, sticky=W)
    Sc = Scrollbar(win)
    Sc.grid(row=3, column=6, sticky = N+S)
    Sc.config(command=lastsub.yview)
    lastsub.config(yscrollcommand=Sc.set)

    qq = Button(win, text = 'Stop', command=win.quit,activeforeground='white',activebackground='red', bg='red', fg='white')
    qq.grid(row=4,column=0)

    dele = Button(win, text = 'del last', command=delsub,activeforeground='black',activebackground='white', bg='white', fg='black')
    dele.grid(row=4,column=1)

    adds = Button(win, text = 'Insert', command=insertsub,activeforeground='black',activebackground='white', bg='white', fg='black')
    adds.grid(row=4,column=2)
    
    win.mainloop() #进入消息循环