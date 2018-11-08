#!/usr/bin/env python3
#导入随机数模块
import random
num = random.randint(1,100)
count = 1
while count<=5:
    answer = int(input('请输入1到100的数字:'))
    if answer>num:
        print("猜大了")
    elif answer<num:
        print("猜小了")
    else:
        print("猜对了")
        break
    count+=1
else:
    print("随机数是:",num)