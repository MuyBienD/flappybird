import pygame
import sys


def load():
    player_path = (
        "assets/sprites/redbird-downflap.png",
        "assets/sprites/redbird-midflap.png",
        "assets/sprites/redbird-upflap.png"
    )

    background_path = "assets/sprites/background-black.png"

    pipe_path = "assets/sprites/pipe-green.png"

    images, sounds, hitmasks = {}, {}, {}

    images["numbers"] = (
        pygame.image.load("assets/sprites/0.png").convert_alpha(),
        pygame.image.load("assets/sprites/1.png").convert_alpha(),
        pygame.image.load("assets/sprites/2.png").convert_alpha(),
        pygame.image.load("assets/sprites/3.png").convert_alpha(),
        pygame.image.load("assets/sprites/4.png").convert_alpha(),
        pygame.image.load("assets/sprites/5.png").convert_alpha(),
        pygame.image.load("assets/sprites/6.png").convert_alpha(),
        pygame.image.load("assets/sprites/7.png").convert_alpha(),
        pygame.image.load("assets/sprites/8.png").convert_alpha(),
        pygame.image.load("assets/sprites/9.png").convert_alpha()
    )

    images["base"] = pygame.image.load("assets/sprites/base.png").convert_alpha()

    if "win32" in sys.platform:
        soundext = ".wav"
    else:
        soundext = ".ogg"

    sounds["die"] = pygame.mixer.Sound("assets/audio/die" + soundext)
    sounds["hit"] = pygame.mixer.Sound("assets/audio/hit" + soundext)
    sounds["point"] = pygame.mixer.Sound("assets/audio/point" + soundext)
    sounds["swoosh"] = pygame.mixer.Sound("assets/audio/swoosh" + soundext)
    sounds["wing"] = pygame.mixer.Sound("assets/audio/wing" + soundext)

    images["background"] = pygame.image.load(background_path).convert()

    images["player"] = (
        pygame.image.load(player_path[0]).convert_alpha(),
        pygame.image.load(player_path[1]).convert_alpha(),
        pygame.image.load(player_path[2]).convert_alpha(),
    )

    images["pipe"] = (
        pygame.transform.rotate(
            pygame.image.load(pipe_path).convert_alpha(),180),
        pygame.image.load(pipe_path).convert_alpha()
    )

    hitmasks["player"] = (
        gethitmask(images["player"][0]),
        gethitmask(images["player"][1]),
        gethitmask(images["player"][2])
    )

    hitmasks["pipe"] = (
        gethitmask(images["pipe"][0]),
        gethitmask(images["pipe"][1])
    )

    return images,sounds,hitmasks



#获取每个像素点的值，并判断透明度，要是透明度为0，则为false,返回外形mask
def gethitmask(image):
    mask =[]
    for x in range(image.get_width()):
        mask.append([])
        for y in range(image.get_height()):
            print(image.get_at((x,y)))
            mask[x].append(bool(image.get_at((x,y))[3]))
    return mask


