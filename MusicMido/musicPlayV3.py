import os, sys
sys.path.append(os.path.dirname(__file__))
from yin_fun import *
import pygame
from mido import Message, MidiFile, MidiTrack  # 不这样写会错


class MusicPlay:
    mid = MidiFile()  # 给自己的文件定的.mid后缀
    track1 = MidiTrack()
    track2 = MidiTrack()
    track3 = MidiTrack()
    track4 = MidiTrack()
    mid.tracks.append(track1)
    mid.tracks.append(track2)
    mid.tracks.append(track3)
    mid.tracks.append(track4)
    tracks = [track1,track2,track3,track4]

    def __init__(self,musicName="mymusic", time=250, instruments=[40], sounds=[80]):
        self.name = musicName.strip().replace(' ', '-')
        self.mainPlay = 0    # 主声部乐器
        self.sound = sounds  # 设置音量 0-127
        self.trackNum = len(instruments)
        if self.trackNum > 4:
            for i in range(0,self.trackNum-4):
                self.mid.tracks.append(track:=MidiTrack())
                self.tracks.append(track)
        self.yin_list = []
        self.pai_list = []
        self.time = time
        self.instruments = instruments  # 设置乐器
        self.mode = 0  # 0：会自动补全不满list长度的音节  1：用户自己补全并且分割声部写入  2：切割全部音符

    
    # 后期设置音量
    def set_sounds(self, sounds):
        self.sound = sounds

    
    def set_mode(self, mode):
        self.mode = mode


    # 添加音符和拍子
    def push_yin_pai(self, yins, pais):
        if self.mode == 0:
            for i,yin in enumerate(yins):
                if type(yin) != list:
                    yins[i] = [yin for j in range(self.trackNum)]
            for i,pai in enumerate(pais):
                if type(pai) != list:
                    pais[i] = [pai for j in range(self.trackNum)]
        self.yin_list.append(yins)
        self.pai_list.append(pais)
        

    def beat(self, time):    # 与mido的拍子互换
        time /= 60 * 1000
        time = 1/time
        return time
    

    def yin_init(self):
        for i,yueqi in enumerate(self.instruments):
            self.tracks[i].append(Message('program_change', channel=0, program=yueqi, time=0))
            self.tracks[i].append(Message('note_off', note=0, velocity=0, time=0, channel=0))
    

    def yin(self, yin, 拍子, 前声部=0,声部=tracks[0],音量=64, channel=0):
        if yin == "0" or yin == 0:
            声部.append(Message('note_on', note=22, velocity=0, time=前声部, channel=channel))
            声部.append(Message('note_off', note=22, velocity=0, time=拍子, channel=channel))
        else:
            if type(yin)== str:
                yin = num(yin)
            声部.append(Message('note_on', note=yin, velocity=音量, time=前声部, channel=channel))
            声部.append(Message('note_off', note=yin, velocity=音量, time=拍子, channel=channel))


    def more_yin(self, 音符, 拍子, time=120,bef=None,声部=tracks):   #多声部版  
        pig = int(self.beat(time))  
        for i in range(len(拍子)):
            if type(拍子[i]) == list:
                for j in range(self.trackNum):
                    if bef == None:
                        self.yin(音符[i][j],拍子[i][j]*pig,音量=self.sound[j],声部=声部[j])
                    else:
                        self.yin(音符[i][j],拍子[i][j]*pig,bef[i][j],音量=self.sound[j],声部=声部[j])
            else:  
                if bef == None:
                    self.yin(音符[i],拍子[i]*pig,声部=声部[0],音量=self.sound[0])
                else:
                    self.yin(音符[i],拍子[i]*pig,bef[i],声部=声部[0],音量=self.sound[0])
        

    # 同时按下多个音符
    def __same_yin(self, 音符:list, 拍子, 声部=0, 音轨=0):
        assert 音符, "音符列表为空"
        pig = int(self.beat(self.time))
        音符 = list(map(lambda x:num(x), 音符))
        for yin in 音符:
            self.tracks[声部].append(Message('note_on', note=yin, velocity=self.sound[声部], time=0, channel=音轨))
        for i,yin in enumerate(音符):
            if i==0:
                self.tracks[声部].append(Message('note_off', note=yin, velocity=self.sound[声部], time=拍子*pig, channel=音轨))
            self.tracks[声部].append(Message('note_off', note=yin, velocity=self.sound[声部], time=0, channel=音轨))


    # 同时敲下多个架子鼓
    def __same_BassDrum_yin(self, 音符:list, 拍子, 声部=0):
        assert 音符, "音符列表为空"
        pig = int(self.beat(self.time))
        # 音符 = list(map(lambda x: num(x), 音符))
        for yin in 音符:
            self.tracks[声部].append(Message('note_on', note=yin, velocity=self.sound[声部], time=0, channel=9))
        for i,yin in enumerate(音符):
            if i==0:
                self.tracks[声部].append(Message('note_off', note=yin, velocity=self.sound[声部], time=拍子*pig, channel=9))
            self.tracks[声部].append(Message('note_off', note=yin, velocity=self.sound[声部], time=0, channel=9))


    # 单一音符
    def divide_yin(self, 音符, 拍子, 声部=0, 音轨=0):
        if type(音符) == str or 音符 == 0:
            pig = int(self.beat(self.time))
            self.yin(音符,拍子*pig,声部=self.tracks[声部],音量=self.sound[声部], channel=音轨)
        else :
            self.__same_yin(音符,拍子,声部,音轨)


    # 单一架子鼓
    def divide_BassDrum_yin(self, 音符, 拍子, 声部=0):
        if type(音符) == int or 音符 == '0':
            pig = int(self.beat(self.time))
            self.yin(音符,拍子*pig,声部=self.tracks[声部],音量=self.sound[声部], channel=9)
        else :
            self.__same_BassDrum_yin(音符,拍子,声部)
    

        # 播放器
    def play_midi(self, file):
        pygame.mixer.music.set_volume(1)
        clock = pygame.time.Clock()
        try:
            pygame.mixer.music.load(file)
        except:
            import traceback

            print(traceback.format_exc())
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            clock.tick(30)


    def play(self):
        self.mid.save(f"{self.name}-music.mid")
        self.play_midi(f"./{self.name}-music.mid")
        os.remove(f"./{self.name}-music.mid")


    def run(self):   # mode 0:多声部一个列表  1:多声部多个列表
        freq = 44100
        bitsize = -16
        channels = 2
        buffer = 1024
        pygame.mixer.init(freq, bitsize, channels, buffer) # 初始化pygame

        # 模式 1
        if self.mode == 0:
            self.yin_init()
            self.more_yin(self.yin_list, self.pai_list, self.time)
        # 模式 2
        if self.mode == 1:
            self.yin_init()
            for i in range(len(self.yin_list[0])):
                for j in range(len(self.yin_list)):
                    if self.pai_list[j][i] == 0: continue
                    self.divide_yin(self.yin_list[j][i], self.pai_list[j][i], 声部=j)
        # 模式 3
        if self.mode == 2:
            pass
        print(self.name)
        self.play()




if __name__ == "__main__":
    mymusic = MusicPlay("唯一",250, [0, 0], [100, 80])
    weiyi = [
        ['5', '5'],['3.', '3.'],['2.', '2.'],['1.', '1.'],['2.', '2.'],['3.', '3.'],  # 6
        ['3.', '3.'],['3.', '3.'],['5', '5'],  # 3
        ['3.', '3.'],['1.', '1.'],['7', '7'],['6', '6'],['7', '7'],['1.', '1.'],['2.', '2.'],  # 7
        ['5', '5'],['3.', '3.'],['2.', '2.'],['2.', '2.'],['3.', '3.'],['5', '5'],  # 6
        ['2.', '2.'],['1.', '1.'],['2.', '2.'],['3.', '3.'],  # 4
        ['3.', '3.'],['1.', '1.'],['7', '7'],['1.', '1.'],  # 4
        ['7', '7'],['7', '7'],['1.', '1.'],['2.', '2.'], # 4
        ['1.','6'],['5.','1.'],['3.','1.'],['5.','3.'],['1.','5'],  # 5
        ['6.','1.'],['5.','1.'],['3.','1.'],['5.','1.'],['5.','7'],  # 5
        ['1.','6'],['6.','1.'],['5.','1.'],['3.','1.'],['5.','5.'],['5.','5.'],  # 6
        ['3.','5'],['2.','2.'],['1.','1.'],['1.','6'],['2.','6'],['3.','6'],['5.','6'],  # 7
        ['7','5'],['7','5'],['1.','5'],['2.','5'],['1.','6'],['6.','1.'],['5.','1.'],['3.','1.'],['5.','5.'],['5.','5.'], # 10
        ['3.','5'],['2.','2.'],['1.','1.'],['6.','1.'],['5.','1.'],['3.','1.'],['2.','7'],  # 7
        ['1.','6'],['6.','1.'],['5.','1.'],['3.','1.'],['5.','5.'],['5.','5.'],  # 6
        ['3.','5'],['2.','5'],['1.','3'],['6.','1.'],['5.','7'],['5.','7'],['3.','5'],['1.','3']  # 8
    ]
    w_pai = [
        [1, 1],[2, 2],[1, 1],[2, 2],[2, 2],[4, 4], # 6
        [1, 1],[2, 2],[6, 6], # 3
        [2, 2],[2, 2],[2, 2],[1, 1],[2, 2],[2, 2],[7, 7],  # 7
        [1, 1],[2, 2],[1, 1],[2, 2],[2, 2],[5, 5], # 6
        [1, 1],[1, 1],[1, 1],[6, 6],  # 4
        [2, 2],[2, 2],[2, 2],[4, 4], # 4
        [2, 2],[2, 2],[1, 1],[2, 2], # 4
        [2,2],[2,2],[4,4],[2,2],[8,8],  # 5
        [2,2],[2,2],[1,1],[2,2],[3,3], # 5
        [2,2],[2,2],[2,2],[1,1],[1,1],[8,8], # 6
        [1,1],[1,1],[4,4],[2,2],[2,2],[1,1],[2,2],  # 7
        [2,2],[2,2],[1,1],[2,2],[2,2],[2,2],[2,2],[1,1],[1,1],[8,8], # 10
        [1,1],[1,1],[4,4],[2,2],[2,2],[2,2],[10,10], # 7
        [2,2],[2,2],[2,2],[1,1],[1,1],[8,8], # 6
        [2,2],[2,2],[2,2],[2,2],[2,2],[2,2],[2,2],[10,10] # 8
    ]

    l1 = []
    l2 = []

    p1 = []
    p2 = []

    for i,j in zip(weiyi,w_pai):
        l1.append(i[0])
        l2.append(i[1])
        p1.append(j[0])
        p2.append(j[1])
    mymusic.set_mode(1)
    mymusic.push_yin_pai(l1, p1)
    mymusic.push_yin_pai(l2, p2)
    mymusic.run()
