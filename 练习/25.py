fib=[0,1]
num=int(input('想生成一个多长的fib数列:'))
for i in range(num-2):
    fib.append(fib[-1]+fib[-2])
print(fib)