# 你并非只能创建10个测试。如果你想尝试做更多的比较，可再编写一些测试，并将它们加入到conditional_tests.py中。
# 对于下面列出的各种测试，至少编写一个结果为True和False的测试。
# 检查两个字符串相等和不等。
# 使用函数lower()的测试。
# 检查两个数字相等、不等、大于、小于、大于等于和小于等于。
# 使用关键字and和or的测试。
# 测试特定的值是否包含在列表中。
# 测试特定的值是否未包含在列表中。

str1 = 'pboc'
str2 = 'PBoC'

print(str1 + ' == ' + str2 + ', ' + str(str1 == str2))
print(str1 + ' != ' + str2 + ', ' + str(str1 != str2))

print(str1 + ' == ' + str2.lower() + ', ' + str(str1 == str2.lower()))
print(str1 + ' != ' + str2.lower() + ', ' + str(str1 != str2.lower()))

num1 = 16
num2 = 18
print(str(num1) + ' == ' + str(num2) + ', ' + str(num1 == num2))
print(str(num1) + ' != ' + str(num2) + ', ' + str(num1 != num2))
print(str(num1) + ' > ' + str(num2) + ', ' + str(num1 > num2))
print(str(num1) + ' < ' + str(num2) + ', ' + str(num1 < num2))
print(str(num1) + ' >= ' + str(num2) + ', ' + str(num1 >= num2))
print(str(num1) + ' <= ' + str(num2) + ', ' + str(num1 <= num2))

print('16 > 18 and 18 > 20, ' + str(16 > 18 and 18 > 20))
print('16 < 18 and 18 > 20, ' + str(16 < 18 and 18 > 20))
print('16 < 18 and 18 < 20, ' + str(16 < 18 and 18 < 20))

print('16 > 18 or 18 > 20, ' + str(16 > 18 or 18 > 20))
print('16 < 18 or 18 > 20, ' + str(16 < 18 or 18 > 20))
print('16 < 18 or 18 < 20, ' + str(16 < 18 or 18 < 20))

nums = list(range(1, 20))
print('nums = ' + str(nums))
print('18 in nums, ' + str(18 in nums))
print('18 not in nums, ' + str(18 not in nums))
print('20 in nums, ' + str(20 in nums))
print('20 not in nums, ' + str(20 not in nums))
