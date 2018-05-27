# 既然你知道了如何遍历字典，现在请整理你为完成练习6-3而编写的代码，将其中的一系列print语句替换为一个遍历字典中的键和值的循环。
# 确定该循环正确无误后，再在词汇表中添加5个Python术语。当你再次运行这个程序时，这些新术语及其含义将自动包含在输出中。

info = {'if': '条件判断',
        'for': '循环语句',
        'print': '打印',
        'str': '强转成字符串',
        'lower': '字符串转为小写'
        }

for word, means in info.items():
    print(word + ': ' + means)
print('\n')

info['in'] = '包含'
info['and'] = '与'
info['or'] = '或'
info['list'] = '列表'
info['set'] = '集合'

for word, means in info.items():
    print(word + ': ' + means)
