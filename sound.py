import pygame as pg


class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.shotgun = pg.mixer.Sound("resources/sound/shotgun.wav")
        self.enemy_pain = pg.mixer.Sound("resources/sound/npc_pain.wav")
        self.enemy_death = pg.mixer.Sound("resources/sound/npc_death.wav")
        self.enemy_shot = pg.mixer.Sound("resources/sound/npc_attack.wav")
        self.theme = pg.mixer.music.load("resources/sound/doom-metal-theme.mp3")
       