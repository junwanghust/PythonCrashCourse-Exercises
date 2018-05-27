# 修改为完成练习6-2而编写的程序，让每个人都可以有多个喜欢的数字，然后将每个人的名字及其喜欢的数字打印出来。

info = {'jack': [16, 66],
        'mike': [18, 78, 99, 88, 77],
        'jason': [17, 9],
        'peter': [88, 56, 45],
        'gates': [66]
        }
for name, numbers in info.items():
        print(name + ': ')
        for num in numbers:
                print(str(num) + ', ')
        print('\n')
