# 在你为完成练习4-1而编写的程序中，创建比萨列表的副本，并将其存储到变量friend_pizzas中，再完成如下任务。
# 在原来的比萨列表中添加一种比萨。
# 在列表friend_pizzas中添加另一种比萨。
# 核实你有两个不同的列表。为此，打印消息“My favorite pizzas are:”，再使用一个for循环来打印第一个列表；
# 打印消息“My friend's favorite pizzas are:”，再使用一个for循环来打印第二个列表。核实新增的比萨被添加到了正确的列表中。

pizza = ['墨西哥风味', '榴莲味', '芝士', '孜然风味']

for pz in pizza:
    print(pz.title())

for pz in pizza:
    print('\n你喜欢' + pz.title() + '披萨？')
print('\n\n喜欢披萨！')

friend_pizzas = pizza[:]

pizza.append('牛肉风味')
friend_pizzas.append('猪肉风味')
print('My favorite pizzas are:')
for pz in pizza:
    print(pz.title())

print("My friend's favorite pizzas are:")
for pz in friend_pizzas:
    print(pz.title())