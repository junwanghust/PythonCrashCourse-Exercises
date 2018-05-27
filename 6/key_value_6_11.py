# 创建一个名为cities的字典，其中将三个城市名用作键；
# 对于每座城市，都创建一个字典，并在其中包含该城市所属的国家、人口约数以及一个有关该城市的事实。
# 在表示每座城市的字典中，应包含country、population和fact等键。将每座城市的名字以及有关它它们的信息都打印出来。

cities = {'new york': {'country': 'USA',
                       'population': 1000,
                       'fact': '1234'},
          'shanghai': {'country': 'China',
                       'population': 2000,
                       'fact': '5678'},
          'sydney': {'country': 'Australia',
                     'population': 3000,
                     'fact': '910jq'}
          }

for city, others in cities.items():
        print(city.title() + ': ')
        for info in others.values():
                print(info)
        print('\n')
