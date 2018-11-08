#!/usr/bin/env python3
y = 1
while y<=9:
    x = 1
    while x<=y:
        print(x,'X',y,'=',x*y,sep='',end=' ')
        x+=1
    print()
    y+=1