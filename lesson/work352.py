import easygui as g
import sys
import os

res = g.fileopenbox(msg=None, title=None, default='E:\\python\\lesson\\*.txt', filetypes=["*.txt"], multiple=False)
with open(res,'r') as f:
    tex1 = f.read()
msg1 = '文件【%s】的内容如下：' % os.path.basename(res)
newmsg = g.textbox(msg = msg1, text = tex1)
if newmsg != tex1:
    msg2 = '检测到文件内容发生改变，请选择以下操作：'
    choices = ['覆盖保存','放弃保存','另存为...']
    cho = g.buttonbox(msg = msg2, choices = choices)
    if cho == '覆盖保存':
        with open(res,'w') as f:
            f.write(newmsg)
    elif cho == '另存为...':
        pos = g.filesavebox(msg = '请选择存放位置', default='default.【txt')
        while True:
            if os.path.isfile(pos):
                g.msgbox("该文件已存在！")
                pos = g.filesavebox(msg = '请重新选择存放位置', default='default',filetypes='*.txt')
            else:
                break
        with open(pos,'w') as f:
            f.write(newmsg)
    else:
        sys.exit(0)

    