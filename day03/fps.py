#!/usr/bin/env python3
def fib(num):
    fibs = [0,1]
    for i in range(num-2):
        fibs.append(fibs[-1]+fibs[-2])
    print(fibs)
#fib(10)
#fib(15)
print(__name__) #保存模块名
fib(8)
fib(12)
#当模块直接执行时__name__的值为'__main__'
#当模块被导入时__name__的值为模块名fps
if __name__=='__main__': #模块主程序
    fib(10)
    fib(13)