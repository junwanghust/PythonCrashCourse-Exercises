# 修改你在练习10-8中编写的except代码块，让程序在文件不存在时一言不发。 

files = ['file\cats.txt', 'file\dogs.txt']

for file in files:
    try:
        with open(file) as fl:
            print(fl.read())
    except FileNotFoundError:
        pass
    print()
