from os import path
from time import strftime
import pickle as p
fname_in='/root/wsw/day06/test_list_money.txt'
#记录格式:时间 支出 收入 余额 备注
sj=strftime('%Y-%m-%d %H:%M:%S')

# def in_if():
#    money_in=input('请输入此笔收入数值:')
#    if money_in.isdigit() and money_in:
#        money_comment=input('请说明该笔收入:')
#        with open(fname_in,'wb+') as in_data:
#            line=len(in_data.readlines())
#            money=in_data.readlines()[line].strip()[3]
#            in_data.writelines([[sj,0,int(money_in),money+int(money_in),money_comment]+'\n'])

def into():
    amount=int(input('amount:'))
    comment=input('comment:')
    with open(fname_in,'rb') as fobj:
        records = p.load(fobj)
        balance = records[-1][-2] + amount
        record=[sj,0,amount,balance,comment]
        records.append(record)

    with open(fname_in,'wb') as fobj:
        p.dump(records,fobj)

# def out_if():
#     money_out = input('请输入此笔支出数值:')
#     if money_out.isdigit() and money_out:
#         money_comment = input('请说明该笔支出:')
#         with open(fname_in, 'wb+') as in_data:
#             line = len(in_data.readlines())
#             money = in_data.readlines()[line][3].strip()
#             in_data.writelines([[sj,int(money_out),0,money-int(money_out),money_comment]+'\n'])

def output():
    amount=int(input('amount:'))
    comment=input('comment:')
    with open(fname_in,'rb') as fobj:
        records = p.load(fobj)
        balance = records[-1][-2] - amount
        record=[sj,amount,0,balance,comment]
        records.append(record)

    with open(fname_in,'wb') as fobj:
        p.dump(records,fobj)

def view_if():
    with open(fname_in, 'rb') as in_data:
        cat=p.load(in_data)
    print('%-20s%-8s%-6s%-15s%-31s'%('时间','支出','收入','余额','备注'))
    for record in cat:
        print('%-22s%-8s%-8s%-12s%-30s'% tuple(record)) #将列表转为元组形式

def menu():
    if not path.exists(fname_in):
        init_data=[[sj,0,0,10000,"开始记录"]]
        with open(fname_in,'wb') as fobj:
            p.dump(init_data,fobj)
    cmds={'0':into,'1':output,'2':view_if}
    tips='''
    (0)记录收入
    (1)记录支出
    (2)查看记录
    (3)quit
    请输入你的选择(0/1/2/3):'''
    while True:
        choice=input(tips).strip()[0]
        if choice not in '0123':
            print('无效输入,请重试')
            continue
        if choice == '3':
            break
        cmds[choice]()


if __name__ == '__main__':
    menu()