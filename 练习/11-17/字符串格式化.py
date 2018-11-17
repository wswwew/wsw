import re
import keyword
print("{} is {} years old".format('bob', 25))
print("{1} is {0} years old".format(25, 'bob'))
print(re.split('\.|-','hello-world.tar.gz')[-1])
for i in keyword.kwlist:
    print(i)