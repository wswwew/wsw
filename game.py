#!/usr/bin/env python3
import random
all_choice = ['剪刀','石头','布']
num_you = 0
num_ai = 0
while num_you<2 and num_ai<2:
    player_num = input('请输入你的选择"剪刀为0 石头为1 布为2":')
    if player_num is None:
        continue
    elif player_num not in ['0','1','2']:
        continue
    player_choice = all_choice[int(player_num)]
    ai_choice = random.choice(all_choice)
    print('电脑出拳为:',ai_choice)
    print('你的出拳为:',player_choice)
    win = ('石头-剪刀','布-石头','剪刀-布')
    lose = ('剪刀-石头','石头-布','布-剪刀')
#print(player_choice+'-'+ai_choice)
    if player_choice+'-'+ai_choice in win:
        print("这局你赢了")
        num_you+=1
    elif player_choice+'-'+ai_choice in lose:
        print("这局你输了")
        num_ai+=1
else:
    if num_you==2:
        print('\n','\n',"你赢了")
    else:
        print('\n','\n',"你输了")