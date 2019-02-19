import urllib.request as ur

response = ur.urlopen('http://www.fishc.com')
html = response.read()
html = html.decode()
print(html[:300])
