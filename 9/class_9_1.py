# 创建一个名为Restaurant的类，其方法__init__()设置两个属性：restaurant_name和cuisine_type。
# 创建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法，
# 其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
# 根据这个类创建一个名为restaurant的实例，分别打印其两个属性，再调用前述两个方法。


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(self.name + ' is a ' + self.type + ' restaurant')

    def open_restaurant(self):
        print(self.name + ' is opened')


restaurant = Restaurant('KFC', 'kaifengcai')
restaurant.open_restaurant()
restaurant.describe_restaurant()
