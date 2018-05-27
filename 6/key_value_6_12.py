# 本章的示例足够复杂，可以以很多方式进行扩展了。
# 请对本章的一个示例进行扩展：添加键和值、调整程序要解决的问题或改进输出的格式。
# many_users.py

users = {'aeinstein': {'first': 'albert',
                       'last': 'einstein',
                       'location': 'princeton'},
         'mcurie': {'first': 'marie',
                    'last': 'curie',
                    'location': 'paris'},
         }

users['test'] = {'first': 'aaa',
                 'last': 'bbb',
                 'location': 'ccc'}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
