# 选择一个你编写的且只包含一个函数的程序，并将这个函数放在另一个文件中。
# 在主程序文件中，使用下述各种方法导入这个函数，再调用它：
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *


# import module_name

import import_lib.printing_functions_8_15

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

import_lib.printing_functions_8_15.print_models(unprinted_designs, completed_models)
import_lib.printing_functions_8_15.show_completed_models(completed_models)


# from module_name import function_name
"""
from import_lib.printing_functions_8_15 import show_completed_models, print_models

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
"""

# from module_name import function_name as fn
"""
from import_lib.printing_functions_8_15 import show_completed_models as scm, print_models as pm

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pm(unprinted_designs, completed_models)
scm(completed_models)
"""

# import module_name as mn
"""
import import_lib.printing_functions_8_15 as pf
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)
"""

# from module_name import *
"""
from import_lib.printing_functions_8_15 import *
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
"""