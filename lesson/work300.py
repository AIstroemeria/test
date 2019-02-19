import os
tys = {}
for files in os.listdir():
    ty = os.path.splitext(files)[1]
    if ty in tys:
        tys[ty] += 1
    else:
        tys[ty] = 0
for keys in tys:
    if keys == '':
        thety = '文件夹'
    else:
        thety = keys
    print("该文件夹下共有类型为【%s】的文件%d个" % (thety, tys[keys]))
