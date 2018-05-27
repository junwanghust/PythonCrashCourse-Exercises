# 创建多个字典，对于每个字典，都使用一个宠物的名称来给它命名；在每个字典中，包含宠物的类型及其主人的名字。
# 将这些字典存储在一个名为pets的列表中，再遍历该列表，并将宠物的所有信息都打印出来。

dolas = {'type': 'dog', 'owner': 'bill'}
pilas = {'type': 'pig', 'owner': 'jack'}
filas = {'type': 'fish', 'owner': 'mike'}

pets = [dolas, pilas, filas]

for pet in pets:
    print(pet['type'].title() + ', ' + pet['owner'].title() )

