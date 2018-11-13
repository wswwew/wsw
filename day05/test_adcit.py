adict ={'name':'bob','age':23}
print('bob' in adict)
print('name'in adict)
for key in adict:
    print('%s:%s'%(key,adict[key]))
print('%(name)s:%(age)s'%adict)