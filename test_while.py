#!/bin/bash/env python3
number = 0
while number<=20:
    number+=1
    if number%2==1:
        continue
    print(number,end=" ")

num = 1
sum10 = 0
while num<=10:
    sum10 = num+sum10
    num+=1
print('\n',sum10,sep='')