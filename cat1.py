# -*- coding: utf-8 -*-
# 範例程式：cat1.py
import pygame
from pygame.locals import *

def show_text(text, x, y):  # 顯示文字的方法，除了顯示文字還能指定位置
    x = x
    y = y
    text = font.render(text, True, (0, 0, 0))
    screen.blit(text, (x, y))
    pygame.display.update()
class MySprite(pygame.sprite.Sprite):
    def __init__(self, target):
      pygame.sprite.Sprite.__init__(self)
      self.target_surface = target
      self.image = None
      self.master_image = None
      self.rect = None
      self.topleft = 0,0
      self.frame = 0
      self.old_frame = -1
      self.frame_width = 1
      self.frame_height = 1     
      self.first_frame = 0
      self.last_frame = 0
      self.columns = 1
      self.last_time = 0

    def load(self, filename, width, height, columns):
      self.master_image = pygame.image.load(filename).convert_alpha()
      self.frame_width = width
      self.frame_height = height
      self.rect = 0,0,width,height
      self.columns = columns
      rect = self.master_image.get_rect()
      self.last_frame = (rect.width // width) * (rect.height // height) - 1
    def update(self, current_time, rate=60):
      if current_time > self.last_time + rate:
        self.frame += 1
        if self.frame > self.last_frame:
            self.frame = self.first_frame
        self.last_time = current_time

      if self.frame != self.old_frame:
        frame_x = (self.frame % self.columns) * self.frame_width
        frame_y = (self.frame // self.columns) * self.frame_height
        rect = ( frame_x, frame_y, self.frame_width, self.frame_height )
        self.image = self.master_image.subsurface(rect)
        self.old_frame = self.frame

mWidth = 800  
mHeight = 600      
pygame.init()
screen = pygame.display.set_mode((mWidth,mHeight),0,32)
pygame.display.set_caption("Sprite 精靈類別測試：one cat")
framerate = pygame.time.Clock()

cat = MySprite(screen)
cat.load("images/sprite.png", 100, 100, 4)
group = pygame.sprite.Group()
group.add(cat)

cat2 = MySprite(screen)
cat2.load("images/sprite.png", 100, 100, 4)
cat2.rect = (200, 200)  # 顯示位置 x,y
group.add(cat2)

cat3 = MySprite(screen)
cat3.load("images/sprite.png", 100, 100, 4)
cat3.rect = (300, 300)  # 顯示位置 x,y
group.add(cat3)
font = pygame.font.Font("fonts/msjh.ttf", 24)  
font.set_bold(True)

while True:
    framerate.tick(30)
    ticks = pygame.time.get_ticks()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
      exit()

    screen.fill((255, 255, 255))
    group.update(ticks)
    group.draw(screen)
    show_text("三隻貓",0,mHeight-30)
    pygame.display.update()