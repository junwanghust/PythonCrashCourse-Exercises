# 如果你还没有在程序中遇到过索引错误，就尝试引引发一个这种错误。
# 在你的一个程序中，修改其中的索引，以引发索引错误。关闭程序前，务必消除这个错误。

names = ['china', 'japan', 'america', 'germany', 'spain', 'africa']

#list index out of range
#print(names[len(names)])

print(names[len(names)-1])
