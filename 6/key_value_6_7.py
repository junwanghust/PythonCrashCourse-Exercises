# 在为完成练习6-1而编写的程序中，再创建两个表示人的字典，然后将这三个字典都存储在一个名为people的列表中。
# 遍历这个列表，将其中每个人的所有信息都打印出来。

info = {'first_name': 'bill', 'last_name': 'gates', 'age': 18, 'city': 'Peking'}
print('first_name: ' + info['first_name'])
print('last_name: ' + info['last_name'])
print('age: ' + str(info['age']))
print('city: ' + info['city'])


info1 = {'first_name': 'bill1', 'last_name': 'gates1', 'age': 19, 'city': 'Tsingtao'}
info2 = {'first_name': 'bill2', 'last_name': 'gates2', 'age': 16, 'city': 'London'}

people = [info, info1, info2]

for pp in people:
    print(pp['first_name'] + ' ' + pp['last_name'] + ' ' + str(pp['age']) + ' ' + pp['city'])
