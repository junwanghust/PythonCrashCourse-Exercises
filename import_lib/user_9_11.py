
class Privileges:

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(self.privileges)


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


class Admin(User):

    def __init__(self, first_name, last_name, age, privileges):
        super(Admin, self).__init__(first_name, last_name, age)
        self.privilege = privileges

