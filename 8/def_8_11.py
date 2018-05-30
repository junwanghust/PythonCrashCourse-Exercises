# 修改你为完成练习8-10而编写的程序，在调用函数make_great()时，向它传递魔术师列表的副本。
# 由于不想修改原始列表，请返回修改后的列表，并将其存储到另一个列表中。
# 分别使用这两个列表来调用show_magicians()，确认一个列表包含的是原来的魔术师师名字，
# 而另一个列表包含的是添加了字样“the Great”的魔术师名字。


def show_magicians(names):
    for nm in names:
        print(nm)


def make_great(names):
    i = 0
    while i < len(names):
        names[i] = 'the Great ' + names[i]
        i += 1
    return names


names = ['lily', 'jack', 'peter', 'pony']
show_magicians(names)
names2 = make_great(names[:])
show_magicians(names)
show_magicians(names2)
