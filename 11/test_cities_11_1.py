# 编写一个函数，它接受两个形参：一个城市名和一个国家名。
# 这个函数返回一个格式为City,Country的字符串，如Santiago,Chile。
# 将这个函数存储在一个名为city_functions.py的模块中。
# 创建一个名为test_cities.py的程序，对刚编写的函数进行测试（别忘了，你需要导入模块unittest以及要测试的函数）。
# 编写一个名为test_city_country()的方法，核实使用类似于'santiago'和'chile'这样的值来调用前述函数时，得到的字符串是正确的。
# 运行test_cities.py，确认测试test_city_country()通过了。

import unittest
from import_lib.city_functions_11_1 import get_city_country


class MyTest(unittest.TestCase):

    def test_city_country(self):
        res = get_city_country('santiago', 'chile')
        self.assertEqual(res, 'Santiago,Chile')

    if __name__ == "__main__":
        unittest.main()
