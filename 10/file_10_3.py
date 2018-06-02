# 编写一个程序，提示用户输入其名字；用户作出响应后，将其名字写入到文件guest.txt中。

name = input('Enter your name: ')

with open('file\guest.txt', 'w') as fw:
    fw.write(name)
