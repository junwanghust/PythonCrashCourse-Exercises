# 管理员是一种特殊的用户。编写一个名为Admin的类，让它继承你为完成练习9-3或练习9-5而编写的User类。
# 添加一个名为privileges的属性，用于存储一个由字符串（如"can add post"、"can delete post"、"can ban user"等）组成的列表。
# 编写一个名为show_privileges()的方法，它显示管理员的权限。创建一个Admin实例，并调用这个方法。

# 9-5


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

    def show_privileges(self):
        print(self.first_name + ' ' + self.last_name + ' ' + self.privilege)


admin = Admin('Z', 'M', '18', 'can add post')
admin.show_privileges()
