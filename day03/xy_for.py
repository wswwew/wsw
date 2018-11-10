#!/usr/bin/env python3
def xy(num):
    for y in range(num+1):
        x = 1
        while x<=y:
            print('%dX%d=%d '%(x,y,x*y),end='')
            #print(x,'X',y,'=',x*y,sep='',end=' ')
            x+=1
        print()
xy(12)