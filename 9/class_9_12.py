# 将User类存储在一个模块中，并将Privileges和Admin类存储在另一个模块中。
# 再创建一个文件，在其中创建一个Admin实例，并对其调用方法show_privileges()，以确认一切都依然能够正确地运行。

from import_lib.other_9_12 import Admin, Privileges

admin = Admin('Z', 'M', '18', Privileges())
admin.privilege.show_privileges()
