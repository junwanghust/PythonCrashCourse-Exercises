# 你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。
# 以完成练习3-6时编写的程序为基础，在程序末尾添加一行代码，打印一条你只能邀请两位嘉宾共进晚餐的消息。
# 使用pop()不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀请他来共进晚餐。
# 对于余下的两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。
# 使用del将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实程序结束时名单确实是空的。

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

print(names.pop()+'抱歉，新餐桌没到，你今晚自己吃饭吧，你是个好人')
print(names.pop(3)+'抱歉，新餐桌没到，你今晚自己吃饭吧，你是个好人')
print(names.pop(2)+'抱歉，新餐桌没到，你今晚自己吃饭吧，你是个好人')
print(names.pop(1)+'抱歉，新餐桌没到，你今晚自己吃饭吧，你是个好人')

print(names[0].title()+'今晚来我家吃饭')
print(names[1].title()+'今晚来我家吃饭')

del names[1]
del names[0]

print(names)
