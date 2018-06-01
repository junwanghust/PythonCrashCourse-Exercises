# 冰淇淋小店是一种特殊的餐馆。编写一个名为IceCreamStand的类，让它继承你为完成练习9-1或练习9-4而编写的Restaurant类。
# 这两个版本的Restaurant类都可以，挑选你更喜欢的那个即可。添加一个名为flavors的属性，用于存储一个由各种口味的冰淇淋组成的列表。
# 编写一个显示这些冰淇淋的方法。创建一个IceCreamStand实例，并调用这个方法。

# 9-4


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self):
        self.number_served += 1

    def describe_restaurant(self):
        print(self.name + ' is a ' + self.type + ' restaurant')

    def open_restaurant(self):
        print(self.name + ' is opened')


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super(IceCreamStand, self).__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show(self):
        print(self.name + ' most famous IceCream is ' + ' ' + self.flavors)


ic = IceCreamStand('KFC', 'Fast Food', 'Chocolate')
ic.show()
