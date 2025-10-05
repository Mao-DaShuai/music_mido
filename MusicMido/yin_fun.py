import mido
from mido import Message, MidiFile, MidiTrack


# 把音名、唱名等换成 MIDO相对应的数字
# 已完成
def num(yin):
    if yin == "A0" or yin == '....6':  # 最低音 la
        return 21
    if yin == "#....6" or yin == "b...7": # 升半音
        return 22
    if yin == "B0" or yin == '....7':  # 最低的si
        return 23
    if yin == "C1" or yin == '...1':  # 低三个八度 do
        return 24
    if yin == "#...1" or yin == "b...2": # 升半音
        return 25
    if yin == "D1" or yin == '...2':  # re
        return 26
    if yin == "#...2" or yin == "b...3": # 升半音
        return 27
    if yin == "E1" or yin == '...3':  # mi
        return 28
    if yin == "F1" or yin == '...4':  # fa
        return 29
    if yin == "#...4" or yin == "b...5": # 升半音
        return 30
    if yin == "G1" or yin == '...5':  # so 或者说 sol
        return 31
    if yin == "#...5" or yin == "b...6": # 升半音
        return 32
    if yin == "A1" or yin == '...6':  # la
        return 33
    if yin == "#...6" or yin == "b...7": # 升半音
        return 34
    if yin == "B1" or yin == '...7':  # si
        return 35
    if yin == "C2" or yin == '..1':  # 低两个八度 do
        return 36
    if yin == "#..1" or yin == "b..2": # 升半音
        return 37
    if yin == "D2" or yin == '..2':  # re
        return 38
    if yin == "#..2" or yin == "b..3": # 升半音
        return 39
    if yin == "E2" or yin == '..3':  # mi
        return 40
    if yin == "F2" or yin == '..4':  # fa
        return 41
    if yin == "#..4" or yin == "b..5": # 升半音
        return 42
    if yin == "G2" or yin == '..5':  # so 或者说 sol
        return 43
    if yin == "#..5" or yin == "b..6": # 升半音
        return 44
    if yin == "A2" or yin == '..6':  # la
        return 45
    if yin == "#..6" or yin == "b..7": # 升半音
        return 46
    if yin == "B2" or yin == '..7':  # si
        return 47
    if (
        yin == "C3"
        or yin == ".do"
        or yin == ".1"
        or yin == ".Do"
        or yin == ".DO"
    ):  # 低八度   do
        return 48
    if yin == "#.1" or yin == "b.2": # 升半音
        return 49
    if (
        yin == "D3"
        or yin == ".re"
        or yin == ".2"
        or yin == ".Re"
        or yin == ".RE"
    ):  # re
        return 50
    if yin == "#.2" or yin == "b.3": # 升半音
        return 51
    if (
        yin == "E3"
        or yin == ".mi"
        or yin == ".3"
        or yin == ".Mi"
        or yin == ".MI"
    ):  # mi
        return 52
    if (
        yin == "F3"
        or yin == ".fa"
        or yin == ".4"
        or yin == ".Fa"
        or yin == ".FA"
    ):  # fa
        return 53
    if yin == "#.4" or yin == "b.5": # 升半音
        return 54
    if (
        yin == "G3"
        or yin == ".so"
        or yin == ".sol"
        or yin == ".5"
        or yin == ".So"
        or yin == ".Sol"
        or yin == ".SO"
        or yin == ".SOL"
    ):  # so 或者说 sol
        return 55
    if yin == "#.5" or yin == "b.6": # 升半音
        return 56
    if (
        yin == "A3"
        or yin == ".la"
        or yin == ".6"
        or yin == ".La"
        or yin == ".LA"
    ):  # la
        return 57
    if yin == "#.6" or yin == "b.7": # 升半音
        return 58
    if (
        yin == "B3"
        or yin == ".si"
        or yin == ".7"
        or yin == ".Si"
        or yin == ".SI"
    ):  # si
        return 59
    # 中音区
    if (
        yin == "C4"
        or yin == "C"
        or yin == "c"
        or yin == "1"
        or yin == 1
        or yin == "do"
        or yin == "Do"
        or yin == "DO"
    ):  # 中音do
        return 60
    if yin == "#1" or yin == "b2": # 升半音
        return 61
    if (
        yin == "D4"
        or yin == "D"
        or yin == "d"
        or yin == "2"
        or yin == 2
        or yin == "re"
        or yin == "Re"
        or yin == "RE"
    ):  # 中音re
        return 62
    if yin == "#2" or yin == "b3": # 升半音
        return 63
    if (
        yin == "E4"
        or yin == "E"
        or yin == "e"
        or yin == "3"
        or yin == 3
        or yin == "mi"
        or yin == "Mi"
        or yin == "MI"
    ):  # 中音mi
        return 64
    if (
        yin == "F4"
        or yin == "F"
        or yin == "f"
        or yin == "4"
        or yin == 4
        or yin == "fa"
        or yin == "Fa"
        or yin == "FA"
    ):  # 中音fa
        return 65
    if yin == "#4" or yin == "b5": # 升半音
        return 66
    if (
        yin == "G4"
        or yin == "G"
        or yin == "g"
        or yin == "5"
        or yin == 5
        or yin == "so"
        or yin == "sol"
        or yin == "So"
        or yin == "Sol"
        or yin == "SO"
        or yin == "SOL"
    ):  # 中音so  或者说 sol
        return 67
    if yin == "#5" or yin == "b6": # 升半音
        return 68
    if (
        yin == "A4"
        or yin == "A"
        or yin == "a"
        or yin == "6"
        or yin == 6
        or yin == "la"
        or yin == "La"
        or yin == "LA"
    ):  # 中音la
        return 69
    if yin == "#6" or yin == "b7": # 升半音
        return 70
    if (
        yin == "B4"
        or yin == "B"
        or yin == "b"
        or yin == "7"
        or yin == 7
        or yin == "si"
        or yin == "Si"
        or yin == "SI"
    ):  # 中音si
        return 71
    # 高音区
    if (
        yin == "C5"
        or yin == "1."
        or yin == "do."
        or yin == "Do."
        or yin == "DO."
    ):  # do
        return 72
    if yin == "#1." or yin == "b2.": # 高音do升半音
        return 73
    if (
        yin == "D5"
        or yin == "2."
        or yin == "re."
        or yin == "Re."
        or yin == "RE."
    ):  # re
        return 74
    if yin == "#2." or yin == "b3.": # 升半音
        return 75
    if (
        yin == "E5"
        or yin == "3."
        or yin == "mi."
        or yin == "Mi."
        or yin == "MI."
    ):  # mi
        return 76
    if (
        yin == "F5"

        or yin == "4."
        or yin == "fa."
        or yin == "Fa."
        or yin == "FA."
    ):  # fa
        return 77
    if yin == "#4." or yin == "b5.": # 升半音
        return 78
    if (
        yin == "G5"
        or yin == "5."
        or yin == "so."
        or yin == "So."
        or yin == "SO."
        or yin == "sol."
        or yin == "Sol."
        or yin == "SOL."
    ):  # so 或者说是 sol
        return 79
    if yin == "#5." or yin == "b6.": # 升半音
        return 80
    if (
        yin == "A5"
        or yin == "6."
        or yin == "la."
        or yin == "La."
        or yin == "LA."
    ):  # la
        return 81
    if yin == "#6." or yin == "b7.": # 升半音
        return 82
    if (
        yin == "B5"
        or yin == "7."
        or yin == "si."
        or yin == "Si."
        or yin == "SI."
    ):  # si
        return 83
    # 从此，退出常用区
    # 高两个八度
    if yin == "C6" or yin == '1..':  # do
        return 84
    if yin == "#1.." or yin == "b2..": # 升半音
        return 85
    if yin == "D6" or yin == '2..':  # re
        return 86
    if yin == "#2.." or yin == "b3..": # 升半音
        return 87
    if yin == "E6" or yin == '3..':  # mi
        return 88
    if yin == "F6" or yin == '4..':  # fa
        return 89
    if yin == "#4.." or yin == "b5..": # 升半音
        return 90
    if yin == "G6" or yin == '5..':  # so
        return 91
    if yin == "#5.." or yin == "b6..": # 升半音
        return 92
    if yin == "A6" or yin == '6..':  # la
        return 93
    if yin == "#6.." or yin == "b7..": # 升半音
        return 94
    if yin == "B6" or yin == '7..':  # si
        return 95
    # 高三个八度
    if yin == "C7" or yin == '1...':  # do
        return 96
    if yin == "#1..." or yin == "b2...": # 升半音
        return 97
    if yin == "D7" or yin == '2...':  # re
        return 98
    if yin == "#2..." or yin == "b3...": # 升半音
        return 99
    if yin == "E7" or yin == '3...':  # mi
        return 100
    if yin == "F7" or  yin == '4...':  # fa
        return 101
    if yin == "#4..." or yin == "b5...": # 升半音
        return 102
    if yin == "G7" or yin == '5...':  # so
        return 103
    if yin == "#5..." or yin == "b6...": # 升半音
        return 104
    if yin == "A7" or yin == '6...':  # la
        return 105
    if yin == "#6..." or yin == "b7...": # 升半音
        return 106
    if yin == "B7" or yin == '7...':  # si
        return 107
    # 高四个八度
    # 最高音do
    if (
        yin == "C8"
        or yin == "highestdo"
        or yin == "hdo"
        or yin == "h1"
        or yin == "highest1"
        or yin == '1....'
    ):  # do
        return 108
