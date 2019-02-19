import urllib.request
import easygui as g
import sys
import os

msg1 = '请填写喵的尺寸'
title1 = '下载一只喵'
fields1 = ['宽：', '高：']
values1 = [400, 600]
while True:
    res = g.multenterbox(msg = msg1, title = title1, fields = fields1, values = values1)

    if res == None:
        sys.exit(0)
    turl = 'http://placekitten.com/g/%s/%s' % (res[0], res[1])
    response = urllib.request.urlopen(turl)
    html = response.read()

    pos1 = g.diropenbox('请选则存放喵的地址：')
    pos1 = os.path.join(pos1, 'cat_%s_%s.jpg' % (res[0], res[1]))

    with open(pos1, 'wb') as f:
        f.write(html)
    
    print(pos1)

    sys.exit(0)

