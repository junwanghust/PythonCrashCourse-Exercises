# 编写一个函数，将一辆汽车的信息存储在一个字典中。这个函数总是接受制造商和型号，还接受任意数量的关键字实参。
# 这样调用这这个函数：提供必不可少的信息，以及两个名称—值对，如颜色和选装配件。
# 这个函数必须能够像下面这样进行调用：car=make_car('subaru','outback',color='blue',tow_package=True)


def make_car(manu, type, **other_info):
    profile = {}
    profile['manu'] = manu
    profile['type'] = type
    for key, value in other_info.items():
        profile[key] = value
    return profile


car_profile = make_car('BMW', 'X5', color='red', price=1000000)
print(car_profile)
