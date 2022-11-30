from sprite_object import *
from enemy import *
import random


class ObjectHandler:

    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.enemy_list = []
        self.enemy_sprite_path = "resources/sprites/npc/"
        self.static_sprite_path = "resources/sprites/static_sprites/"
        self.anim_sprite_path = 'resources/sprites/animated_sprites/'

        # self.add_sprites(SpriteObject(game))
        # self.add_sprites(AnimatedSprite(game))
        # self.add_sprites(AnimatedSprite(game, pos=(10, 7)))
        # self.add_sprites(AnimatedSprite(
        #     game, path=self.anim_sprite_path + "red_light/0.png", pos=(10, 5)))
        self.all_enemy_position = []
        self.random_create_enemy()

    def append_new_enemy(self):
        mini_map = self.game.map.mini_map

        random_y = random.randint(0, len(mini_map) - 1)
        random_x = random.randint(0, len(mini_map[0]) - 1)

        if mini_map[random_y][random_x] == False:
            path = "resources/sprites/npc/cyber_demon/0.png"

            random_sprite = int(random.randint(1, 3))

            if random_sprite == 1:
                path = "resources/sprites/npc/soldier/0.png"
            elif random_sprite == 2:
                path = "resources/sprites/npc/caco_demon/0.png"

            self.all_enemy_position.append({
                "x": int(random_x),
                "y": int(random_y),
                "path": path
            })

    def create_new_enemy(self):
        pass

    def random_create_enemy(self):
        max_enemies = 20

        while True:
            self.append_new_enemy()

            if len(self.all_enemy_position) >= max_enemies:
                break

        for enemy_pos in self.all_enemy_position:
            self.add_enemy(Enemy(self.game, path=enemy_pos["path"], pos=(
                enemy_pos["x"], enemy_pos["y"])))

    def update(self):
        [sprite.update() for sprite in self.sprite_list]
        [enemy.update() for enemy in self.enemy_list]

    def add_enemy(self, enemy):
        self.enemy_list.append(enemy)

    def add_sprites(self, sprite):
        self.sprite_list.append(sprite)
