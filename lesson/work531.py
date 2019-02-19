import urllib.request as ur
import chardet

add = input('请输入url：')
response = ur.urlopen(add).read()
print('该网站使用的编码是:%s' % chardet.detect(response)['encoding'])
