# 编写一个while循环，询问用户为何喜欢编程。每当用户输入一个原因后，都将其添加到一个存储所有原因的文件中。

while True:
    reason = input('why did you like program ?')

    with open('file\why_program.txt', 'a') as fw:
        fw.write(reason + '\n')

    if(input('Continue ? y') == 'y'):
        continue
    else:
        break
