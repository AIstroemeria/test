import urllib.request as ur
import os
import chardet
import socket
import urllib.error

filename = 'urls.txt'
with open(filename, 'r') as f:
    urls = f.readlines()
i = 0
for item in urls:
    try:
        response = ur.urlopen(item)
        html = response.read()
        encoder = chardet.detect(html)['encoding']
        html = html.decode(encoder)
        with open('url_%d.txt' % i,'w', encoding = encoder) as w:
            w.write(html)
    except (socket.gaierror, urllib.error.URLError) as Err:
        with open('url_%d.txt' % i,'w') as w:
            w.write(str(Err))
    i += 1
