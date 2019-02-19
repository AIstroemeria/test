import easygui as g
import sys

msg1 = '''[*真实姓名]为必填项。\r\n
[*手机号码]为必填项。\r\n
[*E-mail]为必填项。\r\n'''
title1 = '账号中心'
fields1 = ['*用户名','*真实姓名','固定电话','*手机号码','QQ','*E-mail']
res = g.multenterbox(msg = msg1, title = title1, fields=fields1)
print(res)

while True:
    if res == None:
        sys.exit(0)
    errmsg = ''
    for i in [0,1,3,5]:
        if res[i].strip() == '':
            errmsg = errmsg + '%s 信息缺失！\r\n' % fields1[i].strip('*')
    if errmsg == '':
        break
    else:
        errmsg = msg1 + errmsg
        res = g.multenterbox(msg =  errmsg, title = title1, fields=fields1)

msg2 = '你输入的信息为：'
for i in range(6):
    msg2 = msg2 + '\r\n' + fields1[i] + '：' + res[i]    
g.msgbox(msg2)