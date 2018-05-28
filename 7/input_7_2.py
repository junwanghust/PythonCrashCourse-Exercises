# 编写一个程序，询问用户有多少人用餐。如果超过8人，就打印一条消息，指出没有空桌；否则指出有空桌。

num = input('how many people ?')
num = int(num)
if num > 8:
    print('No Desktop')
else:
    print('Here is a Desktop')
