member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
score = [88,90,85,90,88]
mem1 = member[:]
for i in range(1,10,2):
    mem1.insert(i,score[(i+-1)//2])
print(mem1)
mem2 = member[:]
