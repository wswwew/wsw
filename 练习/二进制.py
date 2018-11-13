num=int(input('请输入您要转换的数:'))
list=[None]
if num>3:
    max_num=0
    while 2**max_num<=num:
        max_num+=1            #计算出最大位数
    else:
        list[0]=max_num-1
    snum=num-2**list[0]
    count=0       #缓存列表计数器
    for i in range(1,list[0]):
        while 2**i<=snum:
            i+=1
        else:
            list.append(i-1)
            count+=1
            if snum-2**list[count]==1 or snum==1:
                haha=1
                break
            elif snum-2**list[count]>0:
                snum = (snum - 2 ** list[count])
                haha=0
            else:
                haha=0
                break
    print(list)
    long=len(list)
    for x in range(long):
        if list[x]>0:
            haha=10**list[x]+haha
    print(haha)
elif num==3:
    print(list)
    print(11)
else:
    print(list)
    print(num)