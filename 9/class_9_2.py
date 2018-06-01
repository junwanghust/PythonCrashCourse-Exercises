# 根据你为完成练习9-1而编写的类创建三个实例，并对每个实例调用方法describe_restaurant()。


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(self.name + ' is a ' + self.type + ' restaurant')

    def open_restaurant(self):
        print(self.name + ' is opened')


restaurant1 = Restaurant('KFC', 'kaifengcai')
restaurant2 = Restaurant('sha', 'French cuisine')
restaurant3 = Restaurant('ya', 'African cuisine')
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
