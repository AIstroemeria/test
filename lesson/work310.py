import pickle
f = open('record.txt','r')
boy_ = [[]]
girl_ = [[]]
counts = 0
for lines in f:
    if lines[0:3] == '===':
        ft = open('boy_%d.txt' % (counts+1),'wb')
        pickle.dump(boy_[counts],ft)
        ft.close()
        ft = open('girl_%d.txt' % (counts+1),'wb')
        pickle.dump(girl_[counts],ft)
        counts += 1
        boy_.append([])
        girl_.append([])
        ft.close()
    else:
        dia = lines.split(':')
        if dia[0] == '小甲鱼':
            boy_[counts].append(dia[1])
        elif dia[0] == '小客服':
            girl_[counts].append(dia[1])
ft = open('boy_%d.txt' % (counts+1),'wb')
pickle.dump(boy_[counts],ft)
ft.close()
ft = open('girl_%d.txt' % (counts+1),'wb')
pickle.dump(girl_[counts],ft)
ft.close()
