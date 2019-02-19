def findf(tmpdir, tmpfile):
    for items in  os.listdir(tmpdir):
        if items == tmpfile:
            print(os.path.join(tmpdir, tmpfile))
        if os.path.isdir(os.path.join(tmpdir,items)):
            findf(os.path.join(tmpdir, items), tmpfile)    


import os
tmpdir = input("请输入待查找的初始目录:")
tmpfile = input("请输入需要查找的目录文件:")
findf(tmpdir, tmpfile)
