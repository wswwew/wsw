astr='hello world'
alist=[10,20,30]
atuple=('bob','tom','alice')
adict={'name':'bob','phone':137,'age':23}

for a in astr:
    print(a,end='')
print()
for b in alist:
    print(b,end=' ')
print()
for c in atuple:
    print(c,end=' ')
print()
for d in adict:
    print(d,':',adict[d],sep='',end=' ')