# 编写一个while循环，提示用户输入其名字。
# 用户输入其名字后，在屏幕上打印一句问候语，并将一条访问记录添加到文件guest_book.txt中。
# 确保这个文件中的每条记录都独占一行。

while True:
    name = input('Enter your name: ')

    with open('file\guest_book.txt', 'a') as fw:
        fw.write(name + '\n')

    print('Hello ' + name)

    if(input('Continue ? y') == 'y'):
        continue
    else:
        break
