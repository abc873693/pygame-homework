# -*- coding: utf-8 -*-
# 範例程式：pgImage07.py

import pygame, sys

x = 50; y = 400
rocket_width = 200
rocket_height = 46
angle = 15

pygame.init()
background = 'images/cosmic01.png'  # 960x678
pic = 'images/rocket02.png'  # 46x200
screen = pygame.display.set_mode((960,678), 1, 32)
screen.fill([255,255,255])
pygame.display.set_caption('Pygame 顯示圖案')
bg_image = pygame.image.load(background).convert()
image = pygame.image.load(pic).convert_alpha()  # 顯示透明效果

i = 0
while True:
    # 退出事件處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_image, (0,0)) 
    rocket = pygame.transform.rotozoom(image, angle*(-i),1 - 0.20 * i)
    screen.blit(rocket, (x+rocket_width*i, y-rocket_height*i*2))
    i = i + 0.1
    pygame.display.update()
    pygame.time.wait(50)
