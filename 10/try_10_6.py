# 提示用户提供数值输入时，常出现的一个问题是，用户提供的是文本而不是数字。
# 在这种情况下，当你尝试将输入转换为整数时，将引发TypeError异常。
# 编写一个程序，提示用户输入两个数字，再将它们相加并打印结果。
# 在用户输入的任何一个值不是数字时都捕获TypeError异常，并打印一条友好的错误消息。
# 对你编写的程序进行测试：先输入两个数字，再输入一些文本而不是数字。

num1 = input('Enter a number:')
num2 = input('Enter a number:')

try:
    num11 = int(num1)
    num22 = int(num2)
except ValueError:
    print('not a number')
except TypeError:
    print('not a number!')
else:
    print(str(num11+num22))
