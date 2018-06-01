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