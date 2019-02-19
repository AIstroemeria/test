import urllib.request
import re
import os
import string
import random
import html

#open the url and read
def gethtml(url):
    page = urllib.request.urlopen(url)
    html1 = page.read()
    html1 = html.unescape(str(html1))
    page.close()
    return html1

#compile the regular expressions and find
#all stuff we need
def geturl(html1):
    reg = 'data-bind="\{"component":\{"params":\{"schemaVersion":1,"loop":false,"autoPlay":false,"isPlaylistOpen":false,"playlist":\[\{"audioFileUrl":"(.*?)"'
    url_re = re.compile(reg)
    url_list = re.findall(url_re, html1)
    for i in range(len(url_list)):
        url_list[i] = url_list[i].replace('\\\\','')
    return(url_list)

def getmp3(url,path):
    filename = os.path.join(path, url.split('/')[-1])
    req = urllib.request.Request(url)
    req.add_header("User-Agent",randdom_header)
    req.add_header("GET",url)
    u = urllib.request.urlopen(req)
    
    with open(filename, 'wb') as f:
        f.write(u.read())
    print('successful download',' ',filename)
        
def  del_file(path):
      for i in os.listdir(path):
         path_file = os.path.join(path,i)  // 取文件绝对路径
         if os.path.isfile(path_file):
           os.remove(path_file)
         else:
             del_file(path_file)

if __name__ == '__main__':
    os.chdir('E:\python')
    my_headers=[
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",  
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
        ]  
    site = 'https://zh.moegirl.org/%E8%88%B0%E9%98%9FCollection:%E9%87%91%E5%88%9A'
    s = urllib.parse.quote(site,safe = string.printable)
    randdom_header=random.choice(my_headers)
    req = urllib.request.Request(s)
    req.add_header("User-Agent",randdom_header)
    req.add_header("GET",s) 
    html1 = gethtml(req)
    url_list = geturl(html1)

    filepath = os.path.join(os.getcwd(), 'voice')
    if not os.path.exists(filepath):
        del_file(filepath)
        os.mkdir('voice')
    os.chdir(filepath)
    for url in url_list:
        getmp3(url, filepath)

    with open('source.txt','w',encoding='utf-8') as file:
        file.write(html1)
    print(os.getcwd(),'success!')
 