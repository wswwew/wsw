#!/usr/bin/env python3
def xy(num):
    y = 1
    while y<=num:
        x = 1
        while x<=y:
            print(x,'X',y,'=',x*y,sep='',end=' ')
            x+=1
        print()
        y+=1
xy(10)