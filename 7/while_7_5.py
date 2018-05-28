# 有家电影院根据观众的年龄收取不同的票价：
# 不到3岁的观众免费；3~12岁的观众为10美元；超过12岁的观众为15美元。
# 请编写一个循环，在其中询问用户的年龄，并指出其票价。

age = ''
while age != 'quit':
    age = input('enter your age:  \n (enter "quit" to finish)')
    if age != 'quit':
        age = int(age)
        if age <= 3:
            print('Free')
        elif 12 >= age > 3:
            print('10$')
        else:
            print('15$')
