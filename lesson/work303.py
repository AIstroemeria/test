# -*- coding: utf-8 -*-
def findmusic(tmpdir):
    os.chdir(tmpdir)
    for items in os.listdir():
        ty = os.path.splitext(items)[1]
        if ty in ['.flac','.mp3','.m4a','.wma']:
            f = open('E:\\python\\res.txt','a',encoding='UTF-8')
            f.write(os.path.join(os.getcwd(), items)+os.linesep)
            f.close()
        elif os.path.isdir(items):
            findmusic(items)
            os.chdir(os.pardir)
        else:
            pass

import os
tmpdir = input("请输入待查找的初始目录：")
if os.path.exists("E:\\python\\res.txt"):
    os.remove("E:\\python\\res.txt")
findmusic(tmpdir)
