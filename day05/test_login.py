from getpass import getpass
user=dict()
def login_if():
    username = input('请输入用户名:')
    password = getpass('请输入密码:')
    if password == user.get(username) and username and password:
        print('登陆成功')
    else:
        print('登陆失败,请检查用户名或密码')

def signup_if():
    username=input('请输入用户名:')
    if username and username not in user:
        password = getpass('请输入密码:')
        user.update({'%s' % username:'%s'% password})
        print('用户注册成功')
    elif username:
        print('this user is already exist')
    else:
        print('无效用户名,请重新注册登陆')

def show_menu():
    cmds={'0':login_if,'1':signup_if}
    tips='''
    (0)用户登陆
    (1)新用户注册
    (2)quit
    请选择操作(0/1/2):'''
    while True:
        choice=input(tips).strip()[0]
        if choice not in '012':
            print('无效输入,请根据提示进行操作')
            continue
        else:
            if choice == '2':
                break
            cmds[choice]()

if __name__ == '__main__':
    show_menu()