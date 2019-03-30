#coding=utf-8
import  pygame
from pygame.locals import  *
from sys import  exit
import  random

SCREEN_WIDTH=480
SCREEN_HEIGHT=800

class Bullet(pygame.sprite.Sprite):
    def __init__(self,bullet_img,init_pos):
        pygame.sprite.Sprite.__init__(self)
        #super().__init__(self)
        self.image=bullet_img
        self.rect=self.image.get_rect()
        self.rect.midbottom=init_pos
        self.speed=10

    def move(self):
        self.rect.top-=self.speed

class Player(pygame.sprite.Sprite):
    def __init__(self,plane_img,player_rect,init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=[]
        for i in range(len(player_rect)):
            self.image.append(plane_img.subsurface(player_rect[i]).convert_alpha())
        self.rect=player_rect[0]
        self.rect.topleft=init_pos
        self.speed=8
        self.bullets=pygame.sprite.Group()
        self.img_index=0
        self.is_hit=False

    def shoot(self,bullet_img):
        bullet=Bullet(bullet_img,self.rect.midtop)
        self.bullets.add(bullet)

    def moveUp(self):
        if self.rect.top<=0:
            self.rect.top=0
        else:
            self.rect.top-=self.speed

    def moveDown(self):
        if self.rect.top>=SCREEN_HEIGHT-self.rect.height:
            self.rect.top=SCREEN_HEIGHT-self.rect.height
        else:
            self.rect.top+=self.speed

    def moveRight(self):
        if self.rect.left>=SCREEN_WIDTH-self.rect.width:
            self.rect.left=SCREEN_WIDTH-self.rect.width
        else:
            self.rect.left+=self.speed

    def moveLeft(self):
        if self.rect.left<0:
            self.rect.left=0
        else:
            self.rect.left-=self.speed
class Enemy(pygame.sprite.Sprite):
    def __init__(self,enemy_img,enemy_down_img,init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=enemy_img
        self.rect=self.image.get_rect()
        self.rect.topleft=init_pos
        self.down_img=enemy_down_img
        self.speed=2
        self.down_index=0

    def mvoe(self):
        self.rect.top+=self.speed

pygame.init()
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("飞机大战")
ic_launcher=pygame.image.load("resources/image/ic_launcher.png").convert_alpha()
pygame.display.set_icon(ic_launcher)
background=pygame.image.load("resources/image/background.png").convert_alpha()
game_over=pygame.image.load("resources/image/gameover.png").convert_alpha()
plane_img=pygame.image.load("resources/image/shoot.png").convert_alpha()
player=Player(plane_img,)
running=True
while running:
    screen.fill(0)
    screen.blit(background,(0,0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
    key_pressed=pygame.key.get_pressed()
    if key_pressed[K_w] or key_pressed[K_UP]:
        player.moveUp()

