# 编写一个程序，调查用户梦想的度假胜地。
# 使用用类似于“If you could visit one place in the world, where would you go ?”的提示，并编写一个打印调查结果的代码块。

invests = {}

while True:
    msg = input('Did you want to join investigation ? y/n')
    if msg == 'n':
        break
    elif msg == 'y':
        name = input('enter your name: ')
        place = input('If you could visit one place in the world, where would you go ?')
        invests[name] = place
    else:
        print('input error')
        continue
for nm, pla in invests.items():
    print(nm + ' most want go to ' + pla)
