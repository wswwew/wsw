hello = '''Hi
welcome here
wsw'''
print(hello)

hi = 'Hi welcome here wsw'
print(hi)

py_str='python'
print(len(py_str))
print(py_str[::-1])
print('pyton'[0])

a=''
b=None
c='abc'
d='123ggg'
f=12356

#haha=input('f:')
#print(haha)

alist = [1, 2, 3, True, False, 'abc', 1.25, [1, 2, 3]]
print(alist[-1][-1])
print(alist[-3][2])
print('1' in alist)

adict = {'name':'bob','age':18,'address':'bj'}
print(len(adict))

import getpass
username = input('username:')
password = getpass.getpass('password:')
if username == 'bob' and password == '123456':
    print('password is right')
else:
    print('password is wrong')
