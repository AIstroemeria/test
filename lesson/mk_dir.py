import os

names = ['緒形アリシアナ','天王洲なずな','小仏凪','箱部なる','明坂芹菜']
tpath = 'C:\\Users\\hn810\\Desktop\\イロドリミドリ'
os.chdir(tpath)

for i in range(25):
    tmp = str(i)
    if len(tmp) == 1:
        tmp = '0' + tmp
    if not os.path.exists(tmp):
        os.mkdir(tmp)
        os.chdir(tmp)
        for item in names:
            with open('%s.txt' % item,'w') as f:
                pass
        os.chdir(os.pardir)
