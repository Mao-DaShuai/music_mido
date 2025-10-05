from MusicMido.musicPlayV3 import *

music = MusicPlay("Free Lucky",300,[0,0,0],[100,90,100])
music.set_mode(2)
music.yin_init()

# 1
music.divide_yin('.5',2,0)
music.divide_yin('.7',2,0)
music.divide_yin('2',2,0)
music.divide_yin('.7',2,0)
music.divide_yin('.6',2,0)
music.divide_yin('.7',2,0)
music.divide_yin('#.4',2,0)
music.divide_yin('.5',2,0)
music.divide_yin('.1',8,1)
music.divide_yin('.2',8,1)

music.divide_BassDrum_yin('0',16,2)

# 2
music.divide_yin('.5',2,0)
music.divide_yin('.7',2,0)
music.divide_yin('2',2,0)
music.divide_yin('.7',2,0)
music.divide_yin('.6',2,0)
music.divide_yin('.7',2,0)
music.divide_yin('.6',2,0)
music.divide_yin('.5',2,0)
music.divide_yin('.3',8,1)
music.divide_yin('.2',8,1)

music.divide_BassDrum_yin('0',16,2)

# 3
music.divide_yin('.5',2,0)
music.divide_yin('.7',2,0)
music.divide_yin('2',2,0)
music.divide_yin('.7',2,0)
music.divide_yin('.6',2,0)
music.divide_yin('.7',2,0)
music.divide_yin('#.4',2,0)
music.divide_yin('.5',2,0)
music.divide_yin('.1',8,1)
music.divide_yin('.2',8,1)

music.divide_BassDrum_yin('0',16,2)

# 4
music.divide_yin('.5',2,0)
music.divide_yin('.7',2,0)
music.divide_yin('2',2,0)
music.divide_yin('.7',2,0)
music.divide_yin('.6',2,0)
music.divide_yin('.7',2,0)
music.divide_yin('.6',2,0)
music.divide_yin('.5',2,0)
music.divide_yin('.3',8,1)
music.divide_yin('.2',8,1)

music.divide_BassDrum_yin('0',16,2)

# 1
music.divide_yin('.5',2,0)
music.divide_yin('.7',2,0)
music.divide_yin('2',2,0)
music.divide_yin('.7',2,0)
music.divide_yin('.6',2,0)
music.divide_yin('.7',2,0)
music.divide_yin('#.4',2,0)
music.divide_yin('.5',2,0)
music.divide_yin('.1',8,1)
music.divide_yin('.2',8,1)

# 2
music.divide_yin('.5',2,0)
music.divide_yin('.7',2,0)
music.divide_yin('2',2,0)
music.divide_yin('.7',2,0)
music.divide_yin('.6',2,0)
music.divide_yin('.7',2,0)
music.divide_yin('.6',2,0)
music.divide_yin('.5',2,0)
music.divide_yin('.3',8,1)
music.divide_yin('.2',8,1)

# 3
music.divide_yin('.5',2,0)
music.divide_yin('.7',2,0)
music.divide_yin('2',2,0)
music.divide_yin('.7',2,0)
music.divide_yin('.6',2,0)
music.divide_yin('.7',2,0)
music.divide_yin('#.4',2,0)
music.divide_yin('.5',2,0)
music.divide_yin('.1',8,1)
music.divide_yin('.2',8,1)

# 4
music.divide_yin('.5',2,0)
music.divide_yin('.7',2,0)
music.divide_yin('2',2,0)
music.divide_yin('.7',2,0)
music.divide_yin('.6',2,0)
music.divide_yin('.7',2,0)
music.divide_yin('.6',2,0)
music.divide_yin('.5',2,0)
music.divide_yin('.3',8,1)
music.divide_yin('.2',8,1)

for _ in range(4):
    music.divide_BassDrum_yin(36, 2, 2)
    music.divide_BassDrum_yin(44, 2, 2)
    music.divide_BassDrum_yin(38, 2, 2)
    music.divide_BassDrum_yin(44, 2, 2)
    music.divide_BassDrum_yin(36, 2, 2)
    music.divide_BassDrum_yin(44, 2, 2)
    music.divide_BassDrum_yin(38, 2, 2)
    music.divide_BassDrum_yin(44, 2, 2)

music.run()
