# 像练习5-3那样设置外星人的颜色，并编写一个if-else结构。
# 如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了5个点。
# 如果外星人不是绿色的，就打印一条消息，指出玩家获得了10个点。
# 编写这个程序的两个版本，在一个版本中执行if代码块，而在另一一个版本中执行else代码块。

alien_color = 'red'
if alien_color == 'green':
    print('you shot a green alien, get 5 points')
else:
    print('you shot a alien, get 10 points, great!')

alien_color = 'green'
if alien_color == 'green':
    print('you shot a green alien, get 5 points')
else:
    print('you shot a alien, get 10 points, great!')
