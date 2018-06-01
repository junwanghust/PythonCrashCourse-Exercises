# 在练习6-4中，你使用了一个标准字典来表示词汇表。
# 请使用OrderedDict类来重写这个程序，并确认输出的顺序与你在字典中添加键—值对的顺序一致。

from collections import OrderedDict

info = {'if': '条件判断',
        'for': '循环语句',
        'print': '打印',
        'str': '强转成字符串',
        'lower': '字符串转为小写'
        }

orderDict = OrderedDict(info)

orderDict['in'] = '包含'
orderDict['and'] = '与'
orderDict['or'] = '或'
orderDict['list'] = '列表'
orderDict['set'] = '集合'

for word, means in orderDict.items():
    print(word + ': ' + means)
