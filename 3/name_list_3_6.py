# 以完成练习3-4或练习3-5时编写的程序为基础，在程序末尾添加一条print语句，指出你找到了一个更大的餐桌。
# 使用insert()将一位新嘉宾添加到名单开头。
# 使用insert()将另一位新嘉宾添加到名单中间。
# 使用append()将最后一位新嘉宾添加到名单末尾。
# 打印一系列消息，向名单中的每位嘉宾发出邀请。

names = ['pony', 'jack', 'gates']
name_out = names.pop(1)
print(name_out + "无法来吃晚饭了")
names.insert(1, 'jim')
print( names[0].title() + ',' +names[1].title() + ',' +names[2].title() + ',' + "跟我一起吃晚餐.")

names.insert(0, 'mike')
names.insert(2, 'jason')
names.append('lily')
print( names[0].title() + ',' +names[1].title() + ',' +names[2].title() + ',' +names[3].title() +
       ',' +names[4].title() + ',' +names[5].title() + "跟我一起吃晚餐.")

