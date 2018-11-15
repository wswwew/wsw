from random import randint,choice

# def add(x,y):
#     return x+y

# def sub(x,y):
#     return x-y

def exam():
    cmds = {'+':lambda x,y:x+y,'-':lambda x,y:x-y}
    nums = [randint(1,100) for i in range(2)]
    nums.sort(reverse=True)  #降序排列
    op=choice('+-')
    result=cmds[op](*nums) #拆分元组输入
    # if op=='+':
    #     result=nums[0]+nums[1]
    # else:
    #     result = nums[0] - nums[1]
    prompt='%s %s %s =' % (nums[0],op,nums[1])
    counter=0

    while counter<3:
        try:
            answer= int(input(prompt))
        except:
            continue
        if answer==result:
            print('very good')
            break
        print('wrong answer')
        counter+=1
    else:
        print('%s%s'%(prompt,result))

def main():
    while True:
        exam()
        try:
            yn=input('continnu?(y/n):').strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt,EOFError):
            print('\nBye-bye')
            yn='n'

        if yn in 'nN':
            break

if __name__ == '__main__':
    main()