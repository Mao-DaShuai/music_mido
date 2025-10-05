from MusicMido.musicPlayV2 import *

music = MusicPlay("海海海", 400, [0, 0], [100, 80])

music.set_mode(2)

# 1
music.divide_yin("1..", 4, 0)
music.divide_yin(".6", 2, 1)
music.divide_yin("3", 2, 1)
music.divide_yin("#5.", 4, 0)
music.divide_yin("6", 4, 1)
music.divide_yin("#4.", 8, 0)
music.divide_yin(".7", 2, 1)
music.divide_yin("#4", 2, 1)
music.divide_yin("7", 4, 1)

# 2
music.divide_yin("#1..", 2, 0)
music.divide_yin("#2..", 2, 0)
music.divide_yin("#1", 2, 1)
music.divide_yin("#5", 2, 1)
music.divide_yin("3..", 2, 0)
music.divide_yin("2..", 2, 0)
music.divide_yin("#1.", 2, 1)
music.divide_yin("5", 10, 1)
music.divide_yin("7.", 2, 0)
music.divide_yin("3.", 4, 0)
music.divide_yin("7", 2, 0)

# 3
music.divide_yin("#5.", 4, 0)
music.divide_yin(".6", 2, 1)
music.divide_yin("3", 2, 1)
music.divide_yin("3.", 4, 0)
music.divide_yin("6", 4, 1)
music.divide_yin("#4.", 8, 0)
music.divide_yin(".7", 2, 1)
music.divide_yin("#4", 2, 1)
music.divide_yin("7", 4, 1)

# 4
music.divide_yin("3..", 3, 0)
music.divide_yin("#1", 2, 1)
music.divide_yin("#5", 2, 1)
music.divide_yin("#2..", 3, 0)
music.divide_yin("#1.", 2, 1)
music.divide_yin("5", 10, 1)
music.divide_yin("7.", 2, 0)
music.divide_yin("#5.", 2, 0)
music.divide_yin("3.", 4, 0)
music.divide_yin("7", 2, 0)

# 5
music.divide_yin("3..", 4, 0)
music.divide_yin(".6", 2, 1)
music.divide_yin("3", 2, 1)
music.divide_yin("#2..", 4, 0)
music.divide_yin("6", 4, 1)
music.divide_yin("7.", 8, 0)
music.divide_yin(".7", 2, 1)
music.divide_yin("#4", 2, 1)
music.divide_yin("7", 4, 1)

# 6
music.divide_yin("#5.", 3, 0)
music.divide_yin("6.", 3, 0)
music.divide_yin("5.", 2, 0)
music.divide_yin("#1", 2, 1)
music.divide_yin("#5", 2, 1)
music.divide_yin("#1", 2, 1)
music.divide_yin("5", 10, 1)
music.divide_yin("3.", 4, 0)
music.divide_yin("7", 4, 0)

# 7
music.divide_yin("#5.", 8, 0)
music.divide_yin("#4.", 8, 0)
music.divide_yin("#.4", 8, 1)
music.divide_yin("#.5", 8, 1)
music.divide_yin("#1.", 16, 0)
music.divide_yin("#1", 16, 1)

music.run()

