import pygame
from tiles import *
from settings import *
from player import Player
from support import *
from random import randint


class Level:
    def __init__(self, current_level,surface,create_overworld):
        # level data
        self.score = 0
        self.display_surface = surface
        self.health = 100
        self.hit_delay = 25
        self.current_level = current_level
        level_content = levels[current_level]
        level_data = level_content['content']
        self.new_max_level = level_content['unlock']
        self.create_overworld = create_overworld
        # level background
        if self.current_level == 2 or self.current_level == 3:
            self.background_layout = pygame.image.load('Images/graveyard/png/BG.png').convert_alpha()
        else:
            self.background_layout = pygame.image.load('Images/temple/SunsetTempleBackground.png').convert_alpha()
        self.background = pygame.sprite.GroupSingle()
        self.background.add(Background(self.background_layout))
        # object positions
        enemy_layout = import_csv_layout(level_data['enemies'])
        boundary_layout = import_csv_layout(level_data['boundaries'])
        coin_layout = import_csv_layout(level_data['coins'])
        trees_layout = import_csv_layout(level_data['trees'])
        terrain_layout = import_csv_layout(level_data['terrain'])
        player_layout = import_csv_layout(level_data['player'])
        # object sprite groups
        self.player_goal = pygame.sprite.GroupSingle()
        self.death = False
        self.boundaries_group = self.create_tile_group(boundary_layout,'boundaries')
        self.enemies = self.create_tile_group(enemy_layout,'enemies')
        self.coins = self.create_tile_group(coin_layout,'coins')
        self.trees = self.create_tile_group(trees_layout,'trees')
        self.player = pygame.sprite.GroupSingle()
        self.water = pygame.sprite.Group()
        self.player_setup = self.create_player(player_layout,'player')
        self.tiles = self.create_tile_group(terrain_layout,'terrain')
        self.moving_tiles = self.create_moving_group(terrain_layout,'terrain')
        self.world_shift = 0
        self.level_width = screen_width * 2 + (len(player_layout[0]) * tile_size)
        self.water_setup = self.add_water()

    def add_water(self):
        self.water_start = -screen_width
        water_size = 500
        water_num = int(self.level_width / water_size)
        for tile in range(water_num):
            x = tile * water_size + self.water_start
            y = 704
            sprite = Water(water_size,x,y)
            self.water.add(sprite)


    def create_player(self,layout,type):

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                arrow = pygame.image.load('Images/graveyard/png/Objects/ArrowSign.png').convert_alpha()
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == '3':
                    sprite = Player((x,y))
                    self.player.add(sprite)

                if cell == '2':
                    sprite = StaticTile(tile_size,x,y,arrow)
                    self.player_goal.add(sprite)

    def create_moving_group(self,layout,type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell == '23' and type == 'terrain':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    terrain_tile_list = import_cut_graphics('Images/temple/TempleTIles.png')
                    tile_surface = terrain_tile_list[int(cell)]
                    sprite = Mobiletile(tile_size,x,y,tile_surface)
                    sprite_group.add(sprite)
        return sprite_group

    def create_tile_group(self,layout,type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if type == 'terrain' and cell != '23':
                        terrain_tile_list = import_cut_graphics('Images/temple/TempleTIles.png')
                        tile_surface = terrain_tile_list[int(cell)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)

                    if type == 'trees':
                        terrain_tile_list = import_cut_graphics('Images/temple/TempleTIles.png')
                        tile_surface = terrain_tile_list[int(cell)]
                        sprite = StaticTile(tile_size,x,y,tile_surface)

                    if type == 'coins':
                        sprite = Coins(tile_size,x,y)

                    if type == 'enemies':
                        if randint(0,2):
                            sprite = Enemies(tile_size,x,y,'male')
                        else:
                            sprite = Enemies(tile_size,x,y,'female')

                    if type == 'boundaries':
                        sprite = Tile((x,y),tile_size)
                    sprite_group.add(sprite)

        return sprite_group

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < (screen_width/5) and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width - (screen_width/5) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 5

    def animation(self):

        player = self.player.sprite
        if player.direction.y > 1:
            player.status = 'glide'
        elif player.direction.y < 0:
            player.status = 'jump'
        elif player.direction.x != 0 and 0 <= player.direction.y <= 1:
            player.status = 'run'
        else:
            player.status = 'idle'


        if player.status == 'jump':
            player.animations = player.jump_frames
        elif player.status == 'run':
            player.animations = player.run_frames
        elif player.status == 'dead':
            player.animations = player.dead_frames
        elif player.status == 'glide':
            player.animations = player.glide_frames
        elif player.status == 'attack':
            player.animations = player.attack_frames
        elif player.status == 'idle':
            player.animations = player.idle_frames
        player.frame_index += player.animation_speed
        if player.frame_index >= len(player.animations): player.frame_index = 0
        if player.facing_right:
            player.image = player.animations[int(player.frame_index)]
        else:
            player.image= pygame.transform.flip(player.animations[int(player.frame_index)], True, False)


    def horizontal_movement_collision(self):
        if self.hit_delay >= 1:
            self.hit_delay -= 1
        else:
            self.hit_delay = 0

        collidables = self.tiles.sprites() + self.moving_tiles.sprites()
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in collidables:
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

        for sprite2 in self.enemies.sprites():
            if sprite2.rect.colliderect(player.rect) and self.hit_delay == 0:
                self.health -= 8
                self.hit_delay = 50


    def health_bar(self):
        life = pygame.Rect((15),(25),(self.health),(10))
        pygame.draw.rect(self.display_surface,'green',(life))

    def check_death(self):
        player = self.player.sprite
        if player.rect.top >= 750 or self.health <= 0:
            self.death = True


    def verticle_collision(self):
        collidables = self.tiles.sprites() + self.moving_tiles.sprites()
        player = self.player.sprite
        player.apply_gravity()
        for sprite in collidables:
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.direction.y = 0
                    player.rect.top = sprite.rect.bottom

    def state_change(self):
        goal = self.player_goal.sprite
        player = self.player.sprite
        if player.rect.colliderect(goal.rect):
            self.create_overworld(self.current_level,self.new_max_level)

        quit_keys = pygame.key.get_pressed()

        if quit_keys[pygame.K_ESCAPE] or self.death:
            self.create_overworld(self.current_level,1)

    def boundaries(self):
        for enemy in self.enemies.sprites():
            if pygame.sprite.spritecollide(enemy,self.boundaries_group,False):
                enemy.reverse()

        for tile in self.moving_tiles.sprites():
            if pygame.sprite.spritecollide(tile,self.boundaries_group,False):
                tile.reverse()

        for coin in self.coins.sprites():
            if pygame.sprite.spritecollide(coin, self.player, False):
                self.score += 2
                coin.kill()


    def run(self):
        # exit input
        self.check_death()
        self.state_change()
        # draw background
        self.background.draw(self.display_surface)
        # decoration tiles
        self.water.update(self.world_shift)
        self.water.draw(self.display_surface)
        # level tiles
        self.health_bar()
        self.coins.update(self.world_shift)
        self.coins.draw(self.display_surface)
        self.moving_tiles.update(self.world_shift)
        self.moving_tiles.draw(self.display_surface)
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.enemies.update(self.world_shift)
        self.boundaries_group.update(self.world_shift)
        self.boundaries()
        self.enemies.draw(self.display_surface)
        self.trees.update(self.world_shift)
        self.trees.draw(self.display_surface)


        # player
        self.player.update()
        self.player_goal.update(self.world_shift)
        self.player_goal.draw(self.display_surface)
        self.horizontal_movement_collision()
        self.verticle_collision()
        self.animation()
        self.player.draw(self.display_surface)
        self.scroll_x()
