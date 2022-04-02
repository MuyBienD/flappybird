import pygame
import flappy_bird_utils
from itertools import cycle
import sys
import random

fps = 30
screenwidth = 288
screenheight = 512

# 使用pygame之前必须初始化
pygame.init()

fpslock = pygame.time.Clock()

# 设置主屏窗口
screen = pygame.display.set_mode((screenwidth, screenheight))
# 设置窗口的标题，即游戏名称
pygame.display.set_caption("Flappy bird")

images, sounds, hitmasks = flappy_bird_utils.load()
pipegapsize = 100
basey = screenheight * 0.79

player_width = images["player"][0].get_width()
player_height = images["player"][0].get_height()
pipe_width = images["pipe"][0].get_width()
pipe_height = images["pipe"][0].get_height()
background_width = images["background"].get_width()

player_index_gen = cycle([0, 1, 2, 1])


class GameState:
    def __init__(self):
        self.score = self.playerindex = self.loopiter = 0
        self.playerx = int(screenwidth * 0.2)
        self.playery = int((screenheight - player_height) / 2)
        self.basex = 0
        self.baseshift = images["base"].get_width() - background_width

        newpipe1 = getRandomPipe()
        newpipe2 = getRandomPipe()

        self.upperpipes = [
            {"x": screenwidth, "y": newpipe1[0]["y"]},
            {"x": screenwidth + (screenwidth / 2), "y": newpipe2[0]["y"]},
        ]

        self.lowerpipes = [
            {"x": screenwidth, "y": newpipe1[1]["y"]},
            {"x": screenwidth + (screenwidth / 2), "y": newpipe2[1]["y"]},
        ]

        self.pipevelx = -4
        self.pipevely = 0
        self.playermaxvely = 10
        self.playerminvely = -8
        self.playeraccy = 1
        self.playerflapacc = -9
        self.playerflapped = False

    def frame_step(self,input_actions):
        pygame.event.pump()

        reward = 0.1
        terminal = False

        if sum(input_actions) != 1:
            raise  ValueError("多个输入操作!")



def getRandomPipe():
    gapys = [20, 30, 40, 50, 60, 70, 80, 90]  # 上下两根管子之间的宽度
    index = random.randint(0, len(gapys) - 1)
    gapy = gapys[index]

    gapy += int(basey * 0.2)
    pipex = screenwidth + 10

    return [
        {"x": pipex, "y": gapy - pipe_height},  # upper pipe
        {"x": pipex, "y": gapy + pipegapsize}  # lower pipe
    ]


def game():
    while True:
        # 循环获取事件，监听事件状态
        for event in pygame.event.get():
            # 判断用户是否点了"X"关闭按钮,并执行if代码段
            if event.type == pygame.QUIT:
                # 卸载所有模块
                pygame.quit()
                # 终止程序，确保退出程序
                sys.exit()
        pygame.display.flip()  # 更新屏幕内容
