# filename: collision_detect_start.py
import pygame
 
pygame.init() 
screen = pygame.display.set_mode((800,600)) 
pygame.display.set_caption("Collision Detection Start")
 
black = (0,0,0)
white = (255,255,255)
red = (255,25,25) 
clock = pygame.time.Clock()
class MySprite: 
    def __init__(self, x, y, width, height): 
        self.x = x 
        self.y = y 
        self.width = width 
        self.height = height
 
    def render(self): 
        pygame.draw.rect(screen,black,(self.x,self.y,self.width,self.height))
 
rectangle1 = MySprite(100, 50, 100, 100)
rectangle2 = MySprite(300, 50, 100, 100)
moveX,moveY = 0,0
gameLoop = True
while gameLoop:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            gameLoop = False
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_LEFT):
                moveX = -4
            if (event.key == pygame.K_RIGHT):
                moveX = 4
            if (event.key == pygame.K_UP):
                moveY = -4
            if (event.key == pygame.K_DOWN):
                moveY = 4 
        if (event.type == pygame.KEYUP):
            if (event.key == pygame.K_LEFT):          
                moveX = 0        
            if (event.key == pygame.K_RIGHT):
                moveX = 0 
            if (event.key == pygame.K_UP):
                moveY = 0 
            if (event.key == pygame.K_DOWN):
                moveY = 0 
    print(moveX)
    screen.fill(white)
    rectangle1.x += moveX 
    rectangle1.y += moveY 
    rectangle1.render() 
    rectangle2.render() 
    pygame.display.flip() 
    clock.tick(50)
 
pygame.quit()
