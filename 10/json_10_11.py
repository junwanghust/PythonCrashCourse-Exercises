# 编写一个程序，提示用户输入他喜欢的数字，并使用json.dump()将这个数字存储到文件中。
# 再编写一个程序，从文件中读取这个值，并打印消息“I know your favorite number! It's_____.”。

import json

file = 'file\json_num.json'

num = input('Enter your favorite number: ')

try:
    with open(file, 'w') as fl:
        json.dump(num, fl)
except FileNotFoundError:
    print("'" + file + "'" + 'NOT FOUND.')


try:
    with open(file) as fl:
        num = json.load(fl)
except FileNotFoundError:
    print("'" + file + "'" + 'NOT FOUND.')
else:
    print("I know your favorite number! It's " + num)