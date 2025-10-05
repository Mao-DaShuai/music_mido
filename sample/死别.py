from MusicMido.musicPlayV3 import *

music = MusicPlay("死别", 400, [21,21], [100,90])

music.set_mode(2)
music.yin_init()

# 1 + 2
music.divide_yin('3',4,0)
music.divide_yin('2',4,0)
music.divide_yin('1',4,0)
music.divide_yin('5',4,0)
music.divide_yin('0',8,1)
music.divide_yin('..6',2,1)
music.divide_yin('.3',2,1)
music.divide_yin('.6',2,1)
music.divide_yin('.3',2,1)

# 3
music.divide_yin('6',2,0)
music.divide_yin('5',2,0)
music.divide_yin('3',2,0)
music.divide_yin('1',2,0)
music.divide_yin('..2',2,1)
music.divide_yin('..6',2,1)
music.divide_yin('.2',2,1)
music.divide_yin('..6',2,1)

# 4
music.divide_yin('2',2,0)
music.divide_yin('3',1,0)
music.divide_yin('2',1,0)
music.divide_yin('1',2,0)
music.divide_yin('2',2,0)
music.divide_yin('..5',2,1)
music.divide_yin('.2',2,1)
music.divide_yin('.5',2,1)
music.divide_yin('.2',2,1)

# 5
music.divide_yin('3',4,0)
music.divide_yin('1',2,0)
music.divide_yin('.7',2,0)
music.divide_yin('..1',2,1)
music.divide_yin('..5',2,1)
music.divide_yin('.1',2,1)
music.divide_yin('..5',2,1)

# 6
music.divide_yin('1',4,0)
music.divide_yin('3',4,0)
music.divide_yin('..6',2,1)
music.divide_yin('.3',2,1)
music.divide_yin('.6',2,1)
music.divide_yin('.3',2,1)

# 7
music.divide_yin('4',2,0)
music.divide_yin('3',2,0)
music.divide_yin('2',2,0)
music.divide_yin('1',2,0)
music.divide_yin('..2',2,1)
music.divide_yin('..6',2,1)
music.divide_yin('.2',2,1)
music.divide_yin('..6',2,1)

# 8
music.divide_yin('2',2,0)
music.divide_yin('3',1,0)
music.divide_yin('2',1,0)
music.divide_yin('1',2,0)
music.divide_yin('.7',2,0)
music.divide_yin('..5',2,1)
music.divide_yin('.2',2,1)
music.divide_yin('.5',2,1)
music.divide_yin('.2',2,1)

# 9
music.divide_yin('1',4,0)
music.divide_yin('3',2,0)
music.divide_yin('2',2,0)
music.divide_yin('..1',2,1)
music.divide_yin('..5',2,1)
music.divide_yin('.1',2,1)
music.divide_yin('..5',2,1)

# 10
music.divide_yin('1',4,0)
music.divide_yin('5',4,0)
music.divide_yin('..6',2,1)
music.divide_yin('.3',2,1)
music.divide_yin('.6',2,1)
music.divide_yin('.3',2,1)

# 11
music.divide_yin('6',2,0)
music.divide_yin('5',2,0)
music.divide_yin('3',2,0)
music.divide_yin('1',2,0)
music.divide_yin('..2',2,1)
music.divide_yin('..6',2,1)
music.divide_yin('.2',2,1)
music.divide_yin('..6',2,1)

# 12
music.divide_yin('2',2,0)
music.divide_yin('3',1,0)
music.divide_yin('2',1,0)
music.divide_yin('1',2,0)
music.divide_yin('2',2,0)
music.divide_yin('..5',2,1)
music.divide_yin('.2',2,1)
music.divide_yin('.5',2,1)
music.divide_yin('.2',2,1)

# 13
music.divide_yin('3',4,0)
music.divide_yin('.6',2,0)
music.divide_yin('.7',2,0)
music.divide_yin('..1',2,1)
music.divide_yin('..5',2,1)
music.divide_yin('.1',2,1)
music.divide_yin('..5',2,1)

# 14
music.divide_yin('1',4,0)
music.divide_yin('3',4,0)
music.divide_yin('..6',2,1)
music.divide_yin('.3',2,1)
music.divide_yin('.6',2,1)
music.divide_yin('.3',2,1)

# 15
music.divide_yin('4',2,0)
music.divide_yin('3',2,0)
music.divide_yin('2',2,0)
music.divide_yin('1',2,0)
music.divide_yin('..2',2,1)
music.divide_yin('..6',2,1)
music.divide_yin('.2',2,1)
music.divide_yin('..6',2,1)

# 16
music.divide_yin('2',2,0)
music.divide_yin('3',1,0)
music.divide_yin('2',1,0)
music.divide_yin('1',2,0)
music.divide_yin('.7',2,0)
music.divide_yin('..5',2,1)
music.divide_yin('.2',2,1)
music.divide_yin('.5',2,1)
music.divide_yin('.2',2,1)

# 17
music.divide_yin('1',8,0)
music.divide_yin('..1',2,1)
music.divide_yin('..5',2,1)
music.divide_yin('.1',2,1)
music.divide_yin('..5',2,1)


music.run()
