# 以另一种方式完成练习7-4或练习7-5，在程序中采取如下所有做法。
# 在while循环中使用条件测试来结束循环。
# 使用变量active来控制循环结束的时机。
# 使用break语句在用户输入'quit'时退出循环。
# 7-5

age = ''
while age != 'quit':
    age = input('1.enter your age:  \n (enter "quit" to finish)')
    if age != 'quit':
        age = int(age)
        if age <= 3:
            print('Free')
        elif 12 >= age > 3:
            print('10$')
        else:
            print('15$')


age = ''
while True:
    age = input('2.enter your age:  \n (enter "quit" to finish)')
    if age == 'quit':
        break
    else:
        age = int(age)
        if age <= 3:
            print('Free')
        elif 12 >= age > 3:
            print('10$')
        else:
            print('15$')


active = True
age = ''
while active:
    age = input('3.enter your age:  \n (enter "quit" to finish)')
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age <= 3:
            print('Free')
        elif 12 >= age > 3:
            print('10$')
        else:
            print('15$')