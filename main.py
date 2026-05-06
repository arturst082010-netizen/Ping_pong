import pygame
from pygame import *
window = (700, 500)
from time import time as timer
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def __init__(self):
        super().__init__('fff.jpg', 200, 400, 7, 67, 67)
    def update(self):
        keys = key.get_pressed()
        if (keys[K_a] or keys[K_LEFT]) and self.rect.x > 5:
            self.rect.x -= self.speed
        if (keys[K_d] or  keys[K_RIGHT])  and self.rect.x < len_size - 70:
            self.rect.x += self.speed
class Area():

    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y,width, height)
        self.fill_color = back
        if color:
            self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
 
    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)
 
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
    def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Label(Area):

    def set_text(self, text, fsize=12, color=(0,0,0)):
        self.font = pygame.font.SysFont('verdana', fsize)
        self.image = self.font.render(text,True, color)
 
    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        window.blit(self.image,(self.rect.x + shift_x, self.rect.y + shift_y))
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        super().__init__(x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)
      
back = (200, 255, 255)
ball = Picture('aaa.jpg', 160, 200, 50, 50)  
len_size = 700
width_size = 500
window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
clock = time.Clock()
FPS = 67
move_right = False
move_left = False
background = transform.scale(image.load('52.jpg'), (700, 500))
racket_x = 50
racket_y = 150

racket = Picture('fff.jpg', racket_x, racket_y, 30, 100)
rocket1 = Player()
rocket2 = Player()

speed_x = 4
speed_y = 4
start_x = 5
start_y = 5
game = True
finish = False
while game:
    if not finish:
        window.blit(background, (0, 0))
        racket.fill()
        if move_left:
            racket.rect.x -= racket_speed
        if move_right:
            racket.rect.x += racket_speed
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0 or ball.rect.x > 450:
            speed_x *= -1





    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)