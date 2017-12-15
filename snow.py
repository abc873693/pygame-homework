# -*- coding: utf-8 -*-
# 範例程式：snow.py
#呼叫模組
import pygame, sys, random
from pygame.locals import * 
#啟動模組
pygame.init()
#定義顏色
black = (0,0,0)
white = (255,255,255)

#定義視窗大小
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("模擬下雪")
#定義Class (sprite)
class Snow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([2,2])
        self.image.fill(white)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.centery += 1
        if self.rect.centery >= height:
            self.rect.centerx = random.randrange(0, width)
            self.rect.centery = random.randrange(-20, -5)
#建立sprite群組
snow_list = pygame.sprite.Group()
for i in range(50):
    snow_icon = Snow()
    snow_icon.rect.centerx = random.randrange(0, width)
    snow_icon.rect.centery = random.randrange(0, height)
    snow_list.add(snow_icon)
#遊戲迴圈
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(20)  # 數字愈大雪花移動速度愈快
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
	
    screen.fill(black)
    snow_list.draw(screen)
    snow_list.update()
    pygame.display.flip()  # 更新畫面

pygame.quit()  # 結束Pygame
exit()  # 結束Python