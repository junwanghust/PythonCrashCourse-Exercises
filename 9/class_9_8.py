# 编写一个名为Privileges的类，它只有一个属性——privileges，其中存储了练习9-7所说的字符串列表。
# 将方法show_privileges()移到这个类中。在Admin类中，将一个Privileges实例用作其属性。
# 创建一个Admin实例，并使用方法show_privileges()来显示其权限。


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


pri = Privileges()
admin = Admin('Z', 'M', '18', pri)
admin.privilege.show_privileges()
