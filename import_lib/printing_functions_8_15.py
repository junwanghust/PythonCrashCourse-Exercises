# 将示例print_models.py中的函数放在另一个名为printing_functions.py的文件中；
# 在print_models.py的开头编写一条import语句，并修改这个文件以使用导入的函数。


def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
