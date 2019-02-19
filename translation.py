import urllib.request
import urllib.parse
import json

content = input('请输入要翻译的内容:')

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data = {}
data['i']= content
data['from'] ='AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '1539239441228'
data['sign'] = 'e01e116849b38363f7325bbaab8f11f9'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTION'
data['typoResult'] = 'false'
data = urllib.parse.urlencode(data).encode('utf-8')

head={}
head["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"

response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')
res = json.loads(html)
print('翻译结果：%s' % res['translateResult'][0][0]['tgt'])
