member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
for i,item in zip(range(len(member)),member):
    if i % 2 == 0:
        print(item,end =' ')
    else:
        print(item)
print("")
for item in member:
    if isinstance(item, int):
        print(item)
    else:
        print(item,end=' ')
