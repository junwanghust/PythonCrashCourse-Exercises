# 在完成练习3-4~练习3-7时编写的程序之一中，使用len()打印一条消息，指出你邀请了多少位嘉宾来与你共进晚餐。
# 3-6

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


print("我邀请了" + str(len(names)) + "位朋友")