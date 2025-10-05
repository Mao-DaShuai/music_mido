from MusicMido.musicPlayV3 import *

music = MusicPlay("遗失的心跳", 500, [0, 0, 0], [100, 90, 100])
music.set_mode(2)

dong = 36
da = 39

music.divide_yin("0", 2, 0)
music.divide_yin("0", 2, 1)
music.divide_yin("0", 2, 2)

# 1 + 2
music.divide_yin("b7.", 2, 0)
music.divide_yin("b7", 4, 0)
music.divide_yin("b6.", 6, 0)
music.divide_yin("4.", 2, 0)
music.divide_yin("b3.", 18, 0)

music.divide_yin("b.5", 4, 1)
music.divide_yin("b2", 4, 1)
music.divide_yin("b6", 8, 1)
music.divide_yin("b.6", 2, 1)
music.divide_yin("b3", 14, 1)

music.divide_BassDrum_yin(0, 16, 2)
music.divide_BassDrum_yin(0, 16, 2)

# 3 + 4
music.divide_yin("b7.", 2, 0)
music.divide_yin("b7", 4, 0)
music.divide_yin("b6.", 6, 0)
music.divide_yin("4.", 2, 0)
music.divide_yin("b3.", 18, 0)

music.divide_yin(".4", 4, 1)
music.divide_yin("1", 4, 1)
music.divide_yin("b6", 8, 1)
music.divide_yin("b.7", 2, 1)
music.divide_yin("4", 2, 1)
music.divide_yin("b2.", 2, 1)
music.divide_yin("4", 2, 1)
music.divide_yin("1.", 4, 1)
music.divide_yin("b6", 4, 1)

music.divide_BassDrum_yin(0, 16, 2)
music.divide_BassDrum_yin(0, 16, 2)

# 1 + 2
music.divide_yin("b7.", 2, 0)
music.divide_yin("b7", 4, 0)
music.divide_yin("b6.", 6, 0)
music.divide_yin("4.", 2, 0)
music.divide_yin("b3.", 18, 0)

music.divide_yin("b.5", 4, 1)
music.divide_yin("b2", 4, 1)
music.divide_yin("b6", 8, 1)
music.divide_yin("b.6", 2, 1)
music.divide_yin("b3", 14, 1)

music.divide_BassDrum_yin(dong, 4, 2)
music.divide_BassDrum_yin(da, 2, 2)
music.divide_BassDrum_yin(dong, 6, 2)
music.divide_BassDrum_yin(da, 2, 2)
music.divide_BassDrum_yin(0, 2, 2)
music.divide_BassDrum_yin(dong, 4, 2)
music.divide_BassDrum_yin(da, 2, 2)
music.divide_BassDrum_yin(dong, 6, 2)
music.divide_BassDrum_yin(da, 2, 2)
music.divide_BassDrum_yin(0, 2, 2)

# 3 + 4
music.divide_yin("b7.", 2, 0)
music.divide_yin("b7", 4, 0)
music.divide_yin("b6.", 6, 0)
music.divide_yin("4.", 2, 0)
music.divide_yin("b3.", 18, 0)

music.divide_yin(".4", 4, 1)
music.divide_yin("1", 4, 1)
music.divide_yin("b6", 8, 1)
music.divide_yin("b.7", 2, 1)
music.divide_yin("4", 2, 1)
music.divide_yin("b2.", 2, 1)
music.divide_yin("4", 2, 1)
music.divide_yin("1.", 4, 1)
music.divide_yin("b6", 4, 1)

music.divide_BassDrum_yin(dong, 4, 2)
music.divide_BassDrum_yin(da, 2, 2)
music.divide_BassDrum_yin(dong, 6, 2)
music.divide_BassDrum_yin(da, 2, 2)
music.divide_BassDrum_yin(0, 2, 2)
music.divide_BassDrum_yin(dong, 4, 2)
music.divide_BassDrum_yin(da, 2, 2)
music.divide_BassDrum_yin(dong, 6, 2)
music.divide_BassDrum_yin(da, 2, 2)
music.divide_BassDrum_yin(0, 2, 2)


music.run()