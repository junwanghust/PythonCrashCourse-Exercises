# 使用列表解析生成一个列表，其中包含前10个整数的立方。

numbers = [num**3 for num in range(1, 11)]
for num in numbers:
    print(num)

