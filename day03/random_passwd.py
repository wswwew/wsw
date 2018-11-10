#!/usr/bin/env python3
import sys
from string import ascii_letters,digits
def passwd(num):
    from random import choice
    all_choice=ascii_letters+digits+'`~!@#$%^&*(){}_+ -?><":;/.,'
    for i in range(num):
        print(choice(all_choice),end='')

if len(sys.argv)==1:
    rnum=''
else:
    rnum=sys.argv[1]
while rnum.isdigit() is not True:
    rnum=input('请输入所需密码位数:')
    if rnum is '':
        rnum='8'
        break
passwd(int(rnum))
print()