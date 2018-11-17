#!/usr/bin/env python3
import sys
from string import ascii_letters,digits
from random import choice

def gen_pass(num=8):
    all_choice=ascii_letters+digits+'~!@#$%^&*()_,.\][=+|?><":} {-*/'
    #password=''
    password=[]
    for i in range(num):
        data=choice(all_choice)
        #password+=data
        password.append(data)
    password=''.join(password)
    return password

if __name__ == '__main__':
    print(gen_pass())