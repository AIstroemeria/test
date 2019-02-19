import re
import urllib
import http.cookiejar

loginurl = 'https://www.douban.com/accounts/login'
cookie = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))

params = {
"form_email":"hn8100swjcph@live.com",
"form_password":"hn8100swjcph",
"source":"index_nav" #没有的话登录不成功
}

#从首页提交登录
response=opener.open(loginurl, urllib.parse.urlencode(params).encode(encoding='UTF8'))

#验证成功跳转至登录页
if response.geturl() == "https://www.douban.com/accounts/login":
    html=response.read()
    html=html.decode('utf-8')

    #验证码图片地址
    imgurl=re.search('<img id="captcha_image" src="(.+?)" alt="captcha" class="captcha_image"/>', html)
    if imgurl:
        url=imgurl.group(1)
        #将图片保存至同目录下
        res=urllib.request.urlretrieve(url, 'v.jpg')
        #获取captcha-id参数
        captcha=re.search('<input type="hidden" name="captcha-id" value="(.+?)"/>' ,html)
        if captcha:
            vcode=input('请输入图片上的验证码：')
            params["captcha-solution"] = vcode
            params["captcha-id"] = captcha.group(1)
            params["login"] = "登录"
            #提交验证码验证
            response=opener.open(loginurl, urllib.parse.urlencode(params).encode(encoding='UTF8'))
            ''' 登录成功跳转至首页 '''
            if response.geturl() == "https://www.douban.com/":
                print ('login success ! ')
