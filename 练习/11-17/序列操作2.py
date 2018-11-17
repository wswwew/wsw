alist = [10, 'john']
# list(enumerate(alist))  # [(0, 10), (1, 'john')]
# a, b = 0, 10   # a->0  ->10

for ind in range(len(alist)):
    print('%s: %s' % (ind, alist[ind]))

for item in enumerate(alist):
    print('%s: %s' % (item[0], item[1]))

for ind, val in enumerate(alist):
    print('%s: %s' % (ind, val))

atuple = (96, 97, 40, 75, 58, 34, 69, 29, 66, 90)
print(sorted(atuple))
print(sorted('hello'))
print(tuple(reversed(atuple)))
for i in reversed(atuple):
    print('(%s)' % i, end=',')