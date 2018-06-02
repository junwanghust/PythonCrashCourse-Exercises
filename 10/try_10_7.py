# 将你为完成练习10-6而编写的代码放在一个while循环中，让用户犯错（输入的是文本而不是数字）后能够继续输入数字。


while True:
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

    if(input('Continue ? y') == 'y'):
        continue
    else:
        break
