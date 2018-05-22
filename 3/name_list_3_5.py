# 你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。
# 以完成练习3-4时编写的程序为基础，在程序末尾添加一条print语句，指出哪位嘉宾无法赴约。
# 修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
# 再次打印一系列消息，向名单中的每位嘉宾发出邀请。

names = ['pony', 'jack', 'gates']
name_out = names.pop(1)
print(name_out + "无法来吃晚饭了")
names.insert(1, 'jim')
print( names[0].title() + ',' +names[1].title() + ',' +names[2].title() + ',' + "跟我一起吃晚餐.")
