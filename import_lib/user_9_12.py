

class User:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name + ' ' + self.last_name + ' is ' + self.age + ' old')

    def greet_user(self):
        print('Hello ' + self.first_name + ' ' + self.last_name)

