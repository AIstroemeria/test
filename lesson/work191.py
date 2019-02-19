def count(*str1):
    letters = "abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = "1234567890"

    times = 0
    for string in str1:
        clet,cnum,cspa,coth = 0,0,0,0
        times += 1
        for lett in string:
            if lett == " ":
                cspa += 1
            elif lett in letters:
                clet += 1
            elif lett in nums:
                cnum += 1
            else:
                coth += 1
        print("第%d个字符串共有：英文字母%d个，数字%d个，空格%d个，其他字符%d个"\
              % (times, clet, cnum, cspa, coth))


    
                

    
