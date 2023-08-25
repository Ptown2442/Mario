import pygame
from settings import current_level,levels
from tiles import Tile

class Node(pygame.sprite.Sprite):
    def __init__(self,pos,status,icon_speed,node_image):
        super().__init__()
        self.status = status
        lvl0 = pygame.image.load('Images/graveyard/png/Objects/Sign_copy.png').convert_alpha()
        lvl0 = pygame.transform.scale(lvl0, (130,80))
        lvl1 = pygame.image.load('Images/graveyard/png/Objects/Sign_copy_2.png').convert_alpha()
        lvl1 = pygame.transform.scale(lvl1, (130,80))
        lvl2 = pygame.image.load('Images/graveyard/png/Objects/Sign_copy_3.png').convert_alpha()
        lvl2 = pygame.transform.scale(lvl2, (130,80))
        lvl3 = pygame.image.load('Images/graveyard/png/Objects/Sign_copy_4.png').convert_alpha()
        lvl3 = pygame.transform.scale(lvl3, (130,80))
        lvl4 = pygame.image.load('Images/graveyard/png/Objects/Sign_copy_5.png').convert_alpha()
        lvl4 = pygame.transform.scale(lvl4, (130,80))
        lvl5 = pygame.image.load('Images/graveyard/png/Objects/Sign_copy_6.png').convert_alpha()
        lvl5 = pygame.transform.scale(lvl5, (130,80))
        self.frames = [lvl0,lvl1,lvl2,lvl3,lvl4,lvl5]
        self.image = self.frames[node_image]
        if self.status == 'locked':
            self.covered = self.image.copy()
            self.covered.fill('blue',None,pygame.BLEND_RGBA_MULT)
            self.image.blit(self.covered,(0,0))

        self.rect = self.image.get_rect(center=(pos))

        self.detection_zone = pygame.Rect(self.rect.centerx - (icon_speed/2),self.rect.centery - (icon_speed/2),icon_speed,icon_speed)

class Icon(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.pos = pos
        self.image = pygame.image.load('Images/Ninja Girl/idle/Idle__004.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(35,35))
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        self.rect.center = self.pos

class Overworld:
    def __init__(self,start_level,max_level,surface,create_level):
        bg = pygame.image.load('Images/temple/SunsetTempleBackground.png').convert_alpha()
        self.bg = pygame.transform.scale(bg,(1200,704))
        self.display_surface = surface
        self.current_level = start_level
        self.max_level = max_level
        self.create_level = create_level

        # movement logic
        self.moving = False
        self.move_direction = pygame.math.Vector2(0,0)
        self.speed = 8

        # sprites
        self.setup_nodes()
        self.setup_icon()

    def setup_nodes(self):
        self.nodes = pygame.sprite.Group()

        for index, node_data in enumerate(levels.values()):
            if index <= self.max_level:
                node_sprite= Node(node_data['node_pos'],'available',self.speed,index)
            else:
                node_sprite = Node(node_data['node_pos'],'locked',self.speed,index)
            self.nodes.add(node_sprite)

    def draw_paths(self):
        if self.max_level > 0:
            points = [node['node_pos'] for index,node in enumerate(levels.values()) if index <= self.max_level]
            pygame.draw.lines(self.display_surface,'red',False,points,6)

    def setup_icon(self):
        self.icon = pygame.sprite.GroupSingle()
        icon_sprite = Icon(self.nodes.sprites()[self.current_level].rect.center)
        self.icon.add(icon_sprite)

    def input(self):
        keys = pygame.key.get_pressed()

        if not self.moving:
            if keys[pygame.K_RIGHT] and self.current_level < self.max_level:
                self.move_direction = self.get_movement_data('next')
                self.current_level += 1
                self.moving = True
            elif keys[pygame.K_LEFT] and self.current_level > 0:
                self.move_direction = self.get_movement_data('last')
                self.current_level -= 1
                self.moving = True
            elif keys[pygame.K_SPACE]:
                self.create_level(self.current_level)

    def get_movement_data(self,target):
        start = pygame.math.Vector2(self.nodes.sprites()[self.current_level].rect.center)

        if target == 'next':
            end = pygame.math.Vector2(self.nodes.sprites()[self.current_level + 1].rect.center)
        else:
            end = pygame.math.Vector2(self.nodes.sprites()[self.current_level - 1].rect.center)

        return (end - start).normalize()

    def update_icon_pos(self):
        if self.moving and self.move_direction:
            self.icon.sprite.pos += self.move_direction * self.speed
            target_node = self.nodes.sprites()[self.current_level]
            if target_node.detection_zone.collidepoint(self.icon.sprite.pos):
                self.moving = False
                self.move_direction = pygame.math.Vector2(0,0)

    def run(self):
        self.input()
        self.update_icon_pos()
        self.icon.update()
        pygame.Surface.blit(self.display_surface, self.bg, (0, 0))
        self.draw_paths()
        self.nodes.draw(self.display_surface)
        self.icon.draw(self.display_surface)

