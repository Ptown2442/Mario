import sys
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.frame_index = 0
        self.animation_speed = 0.15
        dead1 = pygame.image.load('Images/Ninja Girl/dead/Dead__000.png').convert_alpha()
        dead1 = pygame.transform.scale(dead1, (64, 64))
        dead2 = pygame.image.load('Images/Ninja Girl/dead/Dead__001.png').convert_alpha()
        dead2 = pygame.transform.scale(dead2, (64, 64))
        dead3 = pygame.image.load('Images/Ninja Girl/dead/Dead__002.png').convert_alpha()
        dead3 = pygame.transform.scale(dead3, (64, 64))
        dead4 = pygame.image.load('Images/Ninja Girl/dead/Dead__003.png').convert_alpha()
        dead4 = pygame.transform.scale(dead4, (64, 64))
        dead5 = pygame.image.load('Images/Ninja Girl/dead/Dead__004.png').convert_alpha()
        dead5 = pygame.transform.scale(dead5, (64, 64))
        self.dead_frames = [dead1, dead2, dead3, dead4, dead5]
        idle1 = pygame.image.load('Images/Ninja Girl/idle/Idle__000.png').convert_alpha()
        idle1 = pygame.transform.scale(idle1, (64, 64))
        idle2 = pygame.image.load('Images/Ninja Girl/idle/Idle__001.png').convert_alpha()
        idle2 = pygame.transform.scale(idle2, (64, 64))
        idle3 = pygame.image.load('Images/Ninja Girl/idle/Idle__002.png').convert_alpha()
        idle3 = pygame.transform.scale(idle3, (64, 64))
        idle4 = pygame.image.load('Images/Ninja Girl/idle/Idle__003.png').convert_alpha()
        idle4 = pygame.transform.scale(idle4, (64, 64))
        idle5 = pygame.image.load('Images/Ninja Girl/idle/Idle__004.png').convert_alpha()
        idle5 = pygame.transform.scale(idle5, (64, 64))
        self.idle_frames = [idle1, idle2, idle3, idle4, idle5]
        run1 = pygame.image.load('Images/Ninja Girl/run/Run__001.png').convert_alpha()
        run1 = pygame.transform.scale(run1, (64, 64))
        run2 = pygame.image.load('Images/Ninja Girl/run/Run__002.png').convert_alpha()
        run2 = pygame.transform.scale(run2, (64, 64))
        run3 = pygame.image.load('Images/Ninja Girl/run/Run__003.png').convert_alpha()
        run3 = pygame.transform.scale(run3, (64, 64))
        run4 = pygame.image.load('Images/Ninja Girl/run/Run__004.png').convert_alpha()
        run4 = pygame.transform.scale(run4, (64, 64))
        run5 = pygame.image.load('Images/Ninja Girl/run/Run__005.png').convert_alpha()
        run5 = pygame.transform.scale(run5, (64, 64))
        self.run_frames = [run1, run2, run3, run4, run5]
        glide1 = pygame.image.load('Images/Ninja Girl/glide/Glide_000.png').convert_alpha()
        glide1 = pygame.transform.scale(glide1, (64, 64))
        glide2 = pygame.image.load('Images/Ninja Girl/glide/Glide_001.png').convert_alpha()
        glide2 = pygame.transform.scale(glide2, (64, 64))
        glide3 = pygame.image.load('Images/Ninja Girl/glide/Glide_002.png').convert_alpha()
        glide3 = pygame.transform.scale(glide3, (64, 64))
        glide4 = pygame.image.load('Images/Ninja Girl/glide/Glide_003.png').convert_alpha()
        glide4 = pygame.transform.scale(glide4, (64, 64))
        glide5 = pygame.image.load('Images/Ninja Girl/glide/Glide_004.png').convert_alpha()
        glide5 = pygame.transform.scale(glide5, (64, 64))
        self.glide_frames = [glide1, glide2, glide3, glide4, glide5]
        attack1 = pygame.image.load('Images/Ninja Girl/attack/Attack__000.png').convert_alpha()
        attack1 = pygame.transform.scale(attack1, (64, 64))
        attack2 = pygame.image.load('Images/Ninja Girl/attack/Attack__001.png').convert_alpha()
        attack2 = pygame.transform.scale(attack2, (64, 64))
        attack3 = pygame.image.load('Images/Ninja Girl/attack/Attack__002.png').convert_alpha()
        attack3 = pygame.transform.scale(attack3, (64, 64))
        attack4 = pygame.image.load('Images/Ninja Girl/attack/Attack__003.png').convert_alpha()
        attack4 = pygame.transform.scale(attack4, (64, 64))
        attack5 = pygame.image.load('Images/Ninja Girl/attack/Attack__004.png').convert_alpha()
        attack5 = pygame.transform.scale(attack5, (64, 64))
        self.attack_frames = [attack1, attack2, attack3, attack4, attack5]
        jump1 = pygame.image.load('Images/Ninja Girl/jump/Jump__001.png').convert_alpha()
        jump1 = pygame.transform.scale(jump1, (64, 64))
        jump2 = pygame.image.load('Images/Ninja Girl/jump/Jump__002.png').convert_alpha()
        jump2 = pygame.transform.scale(jump2, (64, 64))
        jump3 = pygame.image.load('Images/Ninja Girl/jump/Jump__003.png').convert_alpha()
        jump3 = pygame.transform.scale(jump3, (64, 64))
        jump4 = pygame.image.load('Images/Ninja Girl/jump/Jump__004.png').convert_alpha()
        jump4 = pygame.transform.scale(jump4, (64, 64))
        jump5 = pygame.image.load('Images/Ninja Girl/jump/Jump__005.png').convert_alpha()
        jump5 = pygame.transform.scale(jump5, (64, 64))
        self.jump_frames = [jump1, jump2, jump3, jump4, jump5]
        self.animations = self.idle_frames
        self.facing_right = True
        self.image = self.animations[self.frame_index]
        self.status = 'idle'
        self.rect = self.image.get_rect(topleft= pos)

        # player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 5
        self.gravity = 0.8
        self.jump_speed = -16

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.jump()


    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y


    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()

