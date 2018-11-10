from random import randint
num = randint(1,10)
num_guess = int(input('请输入猜一个数字:'))
if num_guess > num:
    print('猜大了')
elif num_guess<num:
    print('猜小了')
else:
    print('猜对了')

print('正确的数字为:',num)