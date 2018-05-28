# 让用户输入一个数字，并指出这个数字是否是10的整数

num = input('enter a number: ')
num = int(num)
if num % 10 == 0:
    print(str(num) + ' can divide by 10!')
else:
    print(str(num) + ' can not divide by 10!')
