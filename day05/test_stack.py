box=[]

def push_it(box):
    addt=input('要放入的内容:').strip()
    if addt:   #判断字符串非空
        box.append(addt)
    return  box

def pop_if(box):
    delt=input('要取出的内容:')
    if delt:   #判断字符串非空
        while delt not in box:
            print('内容不在容器内,请重新输入')
            delt = input('要取出的内容:')
        else:
            print('\033[31;1mFrom box,popped: %s\033[0m' % box.pop(box.index(delt)))
    return box

def pop_test():
    if box: #判断,如果列表为非空
        print('\033[31;1mFrom box,popped: %s\033[0m' % box.pop())
    else:
        print('\033[31:1mEmpty box.\033[0m')

def view_if(box):
    for index,alist in enumerate(box):
        print('\033[32;1m%s\033[0m' % str(index+1),'\033[32;1m%s\033[0m' % alist)
    return box

def show_menu():
    cmds = {'0': push_it,'1':pop_if,'2':view_if}
    tips='''
    (0)push it
    (1)pop it
    (2)view it
    (3)quit
    请输入你的选择(0/1/2/3):'''
    print('+'+'*'*50+'+')
    print('+{:^46}+'.format('欢迎使用容器'))
    print('+'+'*'*50+'+')
    while True:
        choice = input(tips).strip()[0]
        if choice not in '0123':
            print('无效输入,请重新输入')
            continue
        cmds[choice](box)  #根据用户的输入,在字典中取出函数,调用
        # if choice == '3':
        #     break
        # if choice == '0':
        #     push_it(box)
        # elif choice == '1':
        #     pop_if(box)
        # else:
        #     view_if(box)

if __name__ == '__main__':
    show_menu()