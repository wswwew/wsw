num=int(input('请输入您要转换的数:'))
max_num=0
list=[None]
while 2**max_num<=num:
    max_num+=1
else:
    list[0]=max_num-1
snum=num-2**list[0]
count=0
for i in range(list[0]):
    while 2**i<=snum:
        i+=1
    else:
        list.append(i-1)
        count+=1
        if snum-2**list[count]>0:
            snum = (snum - 2 ** list[count])
        else:
            break
print(list)
long=len(list)
haha=0
for x in range(long):
    haha=10**list[x]+haha
print(haha)