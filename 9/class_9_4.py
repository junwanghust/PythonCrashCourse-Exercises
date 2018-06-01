# 在为完成练习9-1而编写的程序中，添加一个名为number_served的属性，并将其默认值设置为0。
# 根据这个类创建一个名为restaurant的实例；打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。
# 添加一个名为set_number_served()的方法，它让你能够设置就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值。
# 添加一个名为increment_number_served()的方法，它让你能够将就餐人数递增。
# 调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。


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


restaurant = Restaurant('KFC', 'kaifengcai')
print(str(restaurant.number_served)+' people served in restaurant')

restaurant.number_served = 1
print(str(restaurant.number_served)+' people served in restaurant')

restaurant.set_number_served(15)
print(str(restaurant.number_served)+' people served in restaurant')

restaurant.increment_number_served()
print(str(restaurant.number_served)+' people served in restaurant')


