# 在为完成练习8-7编写的程序中，编写一个while循环，让用户输入一个专辑的歌手和名称。
# 获取这些信息后，使用它们来调用函数make_album()，并将创建的字典打印出来。在这个while循环中，务必要提供退出途径。


def make_album(singer, album, song=''):
    if song:
        return 'Singer: ' + singer + ', Album: ' + album + ', Song: ' + song
    else:
        return 'Singer: ' + singer + ', Album: ' + album


while True:
    singer = input("Input a singer's name:")
    album = input("Input a album's name:")
    song = input("Input a song:")
    print(make_album(singer, album, song))
    info = input("Contine ? y")
    if info == 'y':
        continue
    else:
        break
