# 修改前面(11.1)的函数，使其包含第三个必不可少的形参population，
# 并返回一个格式为City,Country-populationxxx的字符串，如Santiago, Chile - population 5000000。
# 运行test_cities.py，确认测试test_city_country()未通过。
# 修改上述函数，将形参population设置为可选的。再次运行test_cities.py，确认测试test_city_country()又通过了。
# 再编写一个名为test_city_country_population()的测试，
# 核实可以使用类似于'santiago'、'chile'和'population=5000000'这样的值来调用这个函数。
# 再次运行test_cities.py，确认测试test_city_country_population()通过了。

import unittest
from import_lib.city_functions_11_2 import get_city_country


class MyTest(unittest.TestCase):

    def test_city_country(self):
        res = get_city_country('santiago', 'chile')
        self.assertEqual(res, 'Santiago,Chile')

    def test_city_country_population(self):
        res = get_city_country('santiago', 'chile', '5000000')
        self.assertEqual(res, 'Santiago,Chile - Population 5000000')

    if __name__ == "__main__":
        unittest.main()
