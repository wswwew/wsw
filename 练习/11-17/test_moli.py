#class faker_save:
#    def __init__(self,):
alist = []
def save_mod():
    display='''
    请输入你要保存的数据(输入quit退出) >:'''
    while True:
        data=input(display)
        if data == 'quit':
            break
        alist.append(data)
    return alist

def get_mod():
    display='''
    请输入你要提取的数据(输入quit退出) >:'''
    while True:
        data=input(display)
        if data == 'quit':
            break
        if data.isdigit() and alist[int(data)-1]:
            alist.pop(int(data)-1)
        elif data in alist:
            alist.pop(alist.index(data))
        else:
            print('库中无此数据')
    return alist

def view_mod():
    print()
    for i in alist:
        print('%6s %s' % (alist.index(i)+1,i))


def main_loop():
    display='''
    (0) 存储数据
    (1) 提取数据
    (2) 查看数据
    (3) 退出
    请输入您的操作(0/1/2/3):'''
    while True:
        work=input(display).strip()[0]
        if work not in '0123':
            continue
        if work == '3':
            break
        elif work =='2':
            view_mod()
        elif work =='1':
            get_mod()
        else:
            save_mod()

if __name__ == '__main__':
    main_loop()
