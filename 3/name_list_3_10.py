# 想想可存储到列表中的东西，如山岳、河流、国家、城市、语言或你喜欢的任何东西。
# 编写一个程序，在其中创建一个包含这些元素的列表，然后，对于本章介绍的每个函数，都至少使用一次来处理这个列表。

names = ['china', 'japan', 'america', 'germany', 'spain', 'africa']
names.sort()
print(names)
names.sort(reverse=True)
print(names)

sorted(names)
print(names)
sorted(names, reverse=True)
print(names)

names.reverse()
print(names)
names.reverse()
print(names)

print(len(names))
