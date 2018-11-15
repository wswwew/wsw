list_names = ["he", "li", ["liu", "li"], "fu", "chen"]
list_names2 = list_names.copy()
list_names[3] = "平"
print(list_names)
print(list_names2)

name = list_names
print(name)
# 多维列表：，所以2层以后的元素，会跟着原来的列表改变
list_names[2][0] = "高"
print(name)
print(list_names)
print(list_names2)

print()

import copy

# 深拷贝：拷贝的内容 不会随原列表list_names内容的更改而更改
list_names = ["he", "li", ["liu", "li"], "fu", "chen"]
list_names2 = copy.deepcopy(list_names)
list_names[3] = "平"
print(list_names)
print(list_names2)

# 多维列表
list_names[2][0] = "高"
print(list_names)
print(list_names2)