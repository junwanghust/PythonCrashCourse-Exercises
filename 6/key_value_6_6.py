# 在6.3.1节编写的程序favorite_languages.py中执行以下操操作。
# 创建一个应该会接受调查的人员名单，其中有些人已包含在字典中，而其他人未包含在字典中。
# 遍历这个人员名单，对于已参与调查的人，打印一条消息表示感谢。对于还未参与调查的人，打印一条消息邀请他参与调查。

favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
names = ['gate', 'sarah', 'phil', 'test']

for name in names:
    if name in favorite_languages.keys():
        print(name + ', thanks')
    else:
        print(name + ', tell me your favorite language!')

