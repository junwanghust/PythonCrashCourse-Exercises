# 在你为完成练习8-9而编写的程序中，编写一个名为make_great()的函数，对魔术师列表进行修改，
# 在每个魔术师的名字中都加入字样“the Great”。调用函数show_magicians()，确认魔术师列表确实变了。


def show_magicians(names):
    for nm in names:
        print(nm)


def make_great(names):
    i = 0
    while i < len(names):
        names[i] = 'the Great ' + names[i]
        i += 1


names = ['lily', 'jack', 'peter', 'pony']
show_magicians(names)
make_great(names)
show_magicians(names)
