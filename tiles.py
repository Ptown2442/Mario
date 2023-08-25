import pygame
from random import randint
from support import import_cut_graphics


class Background(pygame.sprite.Sprite):
    def __init__(self,bg):
        super().__init__()
        self.image = pygame.transform.scale(bg,(1200,704))
        self.rect = self.image.get_rect(topleft=(0,0))
class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.rect = self.image.get_rect(midbottom=pos)

    def update(self,x_shift):
        self.rect.x += x_shift

class StaticTile(Tile):
    def __init__(self,size,x,y,surface):
        super().__init__((x,y),size)
        self.image = surface
        self.rect = self.image.get_rect(midbottom=(x,y))

class AnimatedTile(Tile):
    def __init__(self,size,x,y):
        super().__init__((x,y),size)
        self.cooldown = 0
        self.cooldown_period = 30
        self.speed = randint(2, 4)
        self.animation_index = 0
        self.frames = [self.image,self.image]
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(x,y))

    def reverse(self):
        if self.cooldown == 0:
            self.speed *= -1
            self.cooldown = self.cooldown_period

    def animation(self):
        if self.cooldown >= 1:
            self.cooldown -= 1
        else:
            self.cooldown = 0
        self.rect.x += self.speed
        self.animation_index += 0.10
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
        if self.speed < 0:
            self.image = pygame.transform.flip(self.image, True, False)

    def update(self, x_shift):
        self.animation()
        self.rect.x += x_shift

class Water(AnimatedTile):
    def __init__(self,size,x,y):
        super().__init__(size,x,y)
        wave1 = pygame.image.load('Images/waterAnimation/waterAnimation1.png').convert_alpha()
        wave1 = pygame.transform.scale(wave1,(500,130))
        wave2 = pygame.image.load('Images/waterAnimation/waterAnimation2.png').convert_alpha()
        wave2 = pygame.transform.scale(wave2,(500,130))
        wave3 = pygame.image.load('Images/waterAnimation/waterAnimation3.png').convert_alpha()
        wave3 = pygame.transform.scale(wave3,(500,130))
        wave4 = pygame.image.load('Images/waterAnimation/waterAnimation4.png').convert_alpha()
        wave4 = pygame.transform.scale(wave4, (500, 130))
        wave5 = pygame.image.load('Images/waterAnimation/waterAnimation5.png').convert_alpha()
        wave5 = pygame.transform.scale(wave5, (500, 130))
        wave6 = pygame.image.load('Images/waterAnimation/waterAnimation6.png').convert_alpha()
        wave6 = pygame.transform.scale(wave6, (500, 130))
        wave7 = pygame.image.load('Images/waterAnimation/waterAnimation7.png').convert_alpha()
        wave7 = pygame.transform.scale(wave7, (500, 130))
        wave8 = pygame.image.load('Images/waterAnimation/waterAnimation8.png').convert_alpha()
        wave8 = pygame.transform.scale(wave8, (500, 130))
        wave9 = pygame.image.load('Images/waterAnimation/waterAnimation9.png').convert_alpha()
        wave9 = pygame.transform.scale(wave9, (500, 130))
        wave10 = pygame.image.load('Images/waterAnimation/waterAnimation10.png').convert_alpha()
        wave10 = pygame.transform.scale(wave10, (500, 130))
        wave11 = pygame.image.load('Images/waterAnimation/waterAnimation11.png').convert_alpha()
        wave11 = pygame.transform.scale(wave11, (500, 130))
        wave12 = pygame.image.load('Images/waterAnimation/waterAnimation12.png').convert_alpha()
        wave12 = pygame.transform.scale(wave12, (500, 130))
        wave13 = pygame.image.load('Images/waterAnimation/waterAnimation13.png').convert_alpha()
        wave13 = pygame.transform.scale(wave13, (500, 130))
        wave14 = pygame.image.load('Images/waterAnimation/waterAnimation14.png').convert_alpha()
        wave14 = pygame.transform.scale(wave14, (500, 130))
        wave15 = pygame.image.load('Images/waterAnimation/waterAnimation15.png').convert_alpha()
        wave15 = pygame.transform.scale(wave15, (500, 130))
        wave16 = pygame.image.load('Images/waterAnimation/waterAnimation16.png').convert_alpha()
        wave16 = pygame.transform.scale(wave16, (500, 130))
        wave17 = pygame.image.load('Images/waterAnimation/waterAnimation17.png').convert_alpha()
        wave17 = pygame.transform.scale(wave17, (500, 130))
        wave18 = pygame.image.load('Images/waterAnimation/waterAnimation18.png').convert_alpha()
        wave18 = pygame.transform.scale(wave18, (500, 130))
        wave19 = pygame.image.load('Images/waterAnimation/waterAnimation19.png').convert_alpha()
        wave19 = pygame.transform.scale(wave19, (500, 130))
        wave20 = pygame.image.load('Images/waterAnimation/waterAnimation20.png').convert_alpha()
        wave20 = pygame.transform.scale(wave20, (500, 130))
        wave21 = pygame.image.load('Images/waterAnimation/waterAnimation21.png').convert_alpha()
        wave21 = pygame.transform.scale(wave21, (500, 130))
        self.speed = 0
        self.frames = [wave1,wave2,wave3,wave4,wave5,wave6,wave7,wave8,wave9,wave10,wave11,wave12,wave13,wave14,wave15,wave16,wave17,wave18,wave19,wave20,wave21]
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(bottomleft=(x,y))

class Coins(AnimatedTile):
    def __init__(self,size,x,y):
        super().__init__(size,x,y)
        coin1 = pygame.image.load('Images/Ninja boy/Kunai.png').convert_alpha()
        coin1 = pygame.transform.scale(coin1,(25,40))
        fincoin1 = pygame.transform.rotate(coin1,(270))
        fincoin2 = pygame.transform.rotate(coin1,(180))
        fincoin3 = pygame.transform.rotate(coin1,(90))
        self.speed = 0
        self.frames = [coin1,fincoin3,fincoin2,fincoin1]
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        ypos = y - size/2
        self.rect = self.image.get_rect(topleft=(x,ypos))

class Mobiletile(AnimatedTile):
    def __init__(self,size,x,y,surface):
        super().__init__(size,x,y)
        img1 = surface
        img1 = pygame.transform.scale(img1,(192,64))
        img2 = surface
        img2 = pygame.transform.scale(img2,(192,64))
        self.animation_index = 0
        self.frames = [img2,img1]
        self.speed = 1
        self.image = self.frames[self.animation_index]
        self.cooldown_period = 55
        self.rect = self.image.get_rect(bottomleft=(x,y))


class Enemies(AnimatedTile):
    def __init__(self,size,x,y,type):
        super().__init__(size,x,y)
        self.damage = 8
        fzomb1 = pygame.image.load('Images/zomb/female/Walk (1).png').convert_alpha()
        fzomb1 = pygame.transform.scale(fzomb1,(64,64))
        fzomb2 = pygame.image.load('Images/zomb/female/Walk (2).png').convert_alpha()
        fzomb2 = pygame.transform.scale(fzomb2, (64, 64))
        fzomb3 = pygame.image.load('Images/zomb/female/Walk (3).png').convert_alpha()
        fzomb3 = pygame.transform.scale(fzomb3, (64, 64))
        fzomb4 = pygame.image.load('Images/zomb/female/Walk (4).png').convert_alpha()
        fzomb4 = pygame.transform.scale(fzomb4, (64, 64))
        fzomb5 = pygame.image.load('Images/zomb/female/Walk (5).png').convert_alpha()
        fzomb5 = pygame.transform.scale(fzomb5, (64, 64))
        fzomb6 = pygame.image.load('Images/zomb/female/Walk (6).png').convert_alpha()
        fzomb6 = pygame.transform.scale(fzomb6, (64, 64))
        zomb6 = pygame.image.load('Images/zomb/male/Walk (6).png').convert_alpha()
        zomb6 = pygame.transform.scale(zomb6, (64,64))
        zomb5 = pygame.image.load('Images/zomb/male/Walk (5).png').convert_alpha()
        zomb5 = pygame.transform.scale(zomb5, (64, 64))
        zomb4 = pygame.image.load('Images/zomb/male/Walk (4).png').convert_alpha()
        zomb4 = pygame.transform.scale(zomb4, (64, 64))
        zomb3 = pygame.image.load('Images/zomb/male/Walk (3).png').convert_alpha()
        zomb3 = pygame.transform.scale(zomb3, (64, 64))
        zomb2 = pygame.image.load('Images/zomb/male/Walk (2).png').convert_alpha()
        zomb2 = pygame.transform.scale(zomb2, (64, 64))
        zomb1 = pygame.image.load('Images/zomb/male/Walk (1).png').convert_alpha()
        zomb1 = pygame.transform.scale(zomb1, (64, 64))
        self.frames = [zomb1,zomb2,zomb3,zomb4,zomb5,zomb6]
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(x,y))
        if type == 'male':
            self.frames = [zomb1,zomb2,zomb3,zomb4,zomb5,zomb6]
        else:
            self.frames = [fzomb1,fzomb2,fzomb3,fzomb4,fzomb5,fzomb6]



