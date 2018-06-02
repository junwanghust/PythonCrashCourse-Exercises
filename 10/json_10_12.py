# 将练习10-11中的两个程序合而为一。如果存储了用户喜欢的数字，就向用户显示它，否则提示用户输入他喜欢的数字并将其存储到文件中。
# 运行这个程序两次，看看它是否像预期的那样工作。

import json

fn = 'file\json_num.json'


def get_num(file):
    try:
        with open(file) as fl:
            return json.load(fl)
    except FileNotFoundError:
        return None
    except ValueError:
        return None


def print_num(file):
    num = get_num(file)
    if num:
        print("I know your favorite number! It's " + num)
    else:
        num = input('Enter your favorite number: ')
        try:
            with open(file, 'w') as fl:
                json.dump(num, fl)
        except FileNotFoundError:
            print("'" + file + "'" + 'NOT FOUND.')


print_num(fn)
