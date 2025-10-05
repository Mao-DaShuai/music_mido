from MusicMido.musicPlayV3 import *

music = MusicPlay("室内系的Track Maker",500,[0,0,0],[127,100,127])
music.set_mode(2)
music.yin_init()

# 1
music.divide_yin('6.',3,0)
music.divide_yin('5.',3,0)
music.divide_yin('1.',2,0)
music.divide_yin('0',2,0)
music.divide_yin('6',2,0)
music.divide_yin('7',2,0)
music.divide_yin('1.',2,0)
music.divide_yin('.4',16,1)

music.divide_yin('0',16,2)

# 2
music.divide_yin('6.',3,0)
music.divide_yin('5.',3,0)
music.divide_yin('7',2,0)
music.divide_yin('0',2,0)
music.divide_yin('5',2,0)
music.divide_yin('7',2,0)
music.divide_yin('1.',2,0)
music.divide_yin('.5',16,1)

music.divide_yin('0',16,2)

# 3
music.divide_yin('6.',3,0)
music.divide_yin('5.',3,0)
music.divide_yin('1.',2,0)
music.divide_yin('0',4,0)
music.divide_yin('1.',2,0)
music.divide_yin('7',2,0)
music.divide_yin('.6',16,1)

music.divide_yin('0',16,2)

# 4
music.divide_yin('1.',3,0)
music.divide_yin('7',3,0)
music.divide_yin('2.',2,0)
music.divide_yin('0',4,0)
music.divide_yin('2.',2,0)
music.divide_yin('6',2,0)
music.divide_yin('.6',16,1)

music.divide_yin('0',16,2)

# 5
music.divide_yin('3.',3,0)
music.divide_yin('5.',3,0)
music.divide_yin('1.',2,0)
music.divide_yin('0',2,0)
music.divide_yin('6',2,0)
music.divide_yin('7',2,0)
music.divide_yin('1.',2,0)
music.divide_yin('.4',16,1)

music.divide_yin('0',16,2)

# 6
music.divide_yin('2.',3,0)
music.divide_yin('3.',3,0)
music.divide_yin('7',2,0)
music.divide_yin('0',2,0)
music.divide_yin('5',2,0)
music.divide_yin('7',2,0)
music.divide_yin('1.',2,0)
music.divide_yin('.5',16,1)

music.divide_yin('0',16,2)

# 7
music.divide_yin('6.',3,0)
music.divide_yin('5.',3,0)
music.divide_yin('1.',2,0)
music.divide_yin('0',4,0)
music.divide_yin('1.',2,0)
music.divide_yin('7',2,0)
music.divide_yin('.6',16,1)

music.divide_yin('0',16,2)

# 8
music.divide_yin('1.',3,0)
music.divide_yin('7',3,0)
music.divide_yin('3',10,0)
music.divide_yin('.6',16,1)

music.divide_yin('0',16,2)

# 9
music.divide_yin('6',3,0)
music.divide_yin('5',3,0)
music.divide_yin('1',2,0)
music.divide_yin('0',2,0)
music.divide_yin('.6',2,0)
music.divide_yin('.7',2,0)
music.divide_yin('1',2,0)
music.divide_yin(['4','.4'],16,1)

n = 1

# 10
music.divide_yin('6',3,0)
music.divide_yin('5',3,0)
music.divide_yin('.7',2,0)
music.divide_yin('0',2,0)
music.divide_yin('.5',2,0)
music.divide_yin('.7',2,0)
music.divide_yin('1',2,0)
music.divide_yin(['..5','...5'],16,1)

n += 1

# 11
music.divide_yin('6',3,0)
music.divide_yin('5',3,0)
music.divide_yin('1',2,0)
music.divide_yin('0',4,0)
music.divide_yin('1',2,0)
music.divide_yin('.7',2,0)
music.divide_yin(['..6','...6'],16,1)

n += 1

# 12
music.divide_yin('1',3,0)
music.divide_yin('.7',3,0)
music.divide_yin('2',2,0)
music.divide_yin('0',4,0)
music.divide_yin('2',2,0)
music.divide_yin('.6',2,0)
music.divide_yin(['..6','...6'],16,1)

n += 1

# 13
music.divide_yin('3',3,0)
music.divide_yin('5',3,0)
music.divide_yin('1',2,0)
music.divide_yin('0',2,0)
music.divide_yin('.6',2,0)
music.divide_yin('.7',2,0)
music.divide_yin('1',2,0)
music.divide_yin(['..4','...4'],16,1)

n += 1

# 14
music.divide_yin('2',3,0)
music.divide_yin('3',3,0)
music.divide_yin('.7',2,0)
music.divide_yin('0',2,0)
music.divide_yin('.5',2,0)
music.divide_yin('.7',2,0)
music.divide_yin('1',2,0)
music.divide_yin(['..5','...5'],16,1)

n += 1

# 15
music.divide_yin('6',3,0)
music.divide_yin('5',3,0)
music.divide_yin('1',2,0)
music.divide_yin('0',4,0)
music.divide_yin('1',2,0)
music.divide_yin('.7',2,0)
music.divide_yin(['..6','...6'],16,1)

n += 1

# 16
music.divide_yin('1',3,0)
music.divide_yin('.7',3,0)
music.divide_yin('.3',10,0)

n += 1


for _ in range(n):
    music.divide_BassDrum_yin([36,44], 2, 2)
    music.divide_BassDrum_yin(44, 2, 2)
    music.divide_BassDrum_yin([38,44], 2, 2)
    music.divide_BassDrum_yin(44, 2, 2)
    music.divide_BassDrum_yin([36,44], 2, 2)
    music.divide_BassDrum_yin(44, 2, 2)
    music.divide_BassDrum_yin([38,44], 2, 2)
    music.divide_BassDrum_yin(44, 2, 2)


music.run()
