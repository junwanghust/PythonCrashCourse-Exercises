# 修改函数make_shirt()，使其在默认情况下制作一件印印有字样“I love Python”的大号T恤。
# 调用这个函数来制作如下T恤：一件印有默认字样的大号T恤、一件印有默认字样的中号T恤和一件印有其他字样的T恤（尺码无关紧要）。


def make_shirt(size, words='I love Python'):
    print('Shirt size is ' + size + ', ' + words)


make_shirt('L')
make_shirt(size='M')
make_shirt(words='I love PHP.', size='XXL')
