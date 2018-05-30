# 编写一个名为make_shirt()的函数，它接受一个尺码以及要印到T恤上的字样。
# 这个函数应打印一个句子，概要地说明T恤的尺码和字样。
# 使用位置实参调用这个函数来制作一件T恤；再使用关键字实参来调用这个函数。


def make_shirt(size, words):
    print('Shirt size is ' + size + ', ' + words)


make_shirt('M', 'I love python.')

make_shirt(size='L', words='I love python!')
make_shirt(words='I love python?', size='XXL')
