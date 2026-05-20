import pygame
 

pygame.init()
from random import randint
from pygame import *
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
        super().__init__('rocket.png', 200, 400, 7, 67, 67)
    def update(self):
        keys = key.get_pressed()
        if (keys[K_a] or keys[K_LEFT]) and self.rect.x > 5:
            self.rect.x -= self.speed
        if (keys[K_d] or  keys[K_RIGHT])  and self.rect.x < len_size - 70:
            self.rect.x += self.speed
    #     if (keys[K_w] or keys[K_UP]) and self.rect.y > 5:
    #         self.rect.y -= self.speed
    #     if (keys[K_s] or keys[K_DOWN]) and self.rect.y < width_size - 70:
    #         self.rect.y += self.speed
    def fire(self):
        keys = key.get_pressed()
        if (keys[K_SPACE]):
            bullet = Bullet(self.rect.centerx, self.rect.top)
            bullets.add(bullet)
            fire.play()
    def set_speed(self, level):
        speeds = [5, 6, 7, 8, 67, 76]
        self.speed = speeds[level]
            

class Enemy(GameSprite):
    def __init__(self):
        super().__init__('ufo.png', randint(0, 630), 0, randint(1, 3), 70, 40) 
    def update(self):
        if self.rect.y <= width_size:
            self.rect.y += self.speed
        else:
            global miss_num
            self.rect.y = 0
            self.rect.x = randint(0, 650)
            self.speed = randint(1, 3)
            miss_num += 1

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
    def __init__(self, filename, x=0, y=0, width=10, height=10,speed = 4):
        super().__init__(x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def update(self):
        keys = key.get_pressed()
        if (keys[K_w] or keys[K_UP]) and self.rect.x > 5 and self.rect.y > 10:
            self.rect.x -= self.speed
        if (keys[K_s] or  keys[K_DOWN])  and self.rect.x < 700 - 70 and self.rect.y < width_size - 120:
            self.rect.x += self.speed
class Ball(sprite.Sprite):
    def __init__(self, x, y, width, height, picture):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load(picture), (width, height)
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Wall(sprite.Sprite):
    def __init__(self, wall_x, wall_y, width, height, color1, color2, color3, speed):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
        self.speed = speed
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 
    def update(self):
        keys = key.get_pressed()
        if (keys[K_w] or keys[K_LEFT]) and self.rect.y > 10:
            self.rect.y -= self.speed
        if (keys[K_s] or  keys[K_RIGHT])  and self.rect.y < width_size - 120:
            self.rect.y += self.speed
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
class Enemy_wall(sprite.Sprite) :
    def __init__(self, wall_x, wall_y, width, height, color1, color2, color3, speed):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
        self.speed = speed
        self.direction = 'right'
        self.road = (0, 380)
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
    def update(self):
        if self.rect.y <= self.road[0]:
            self.direction = 'right'
        if self.rect.y > self.road[1]:
            self.direction = 'left'
        if self.direction == 'right':
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed

back = (200, 255, 255)
window = pygame.display.set_mode((700, 500))
image = pygame.transform.scale(pygame.image.load('52.jpg'), (700, 500))

len_size = 700
width_size = 500
clock = pygame.time.Clock()
wall1 = Wall(20, 190, 15, 60, 58, 219, 0, 15)
wall2 = Enemy_wall(650, 190, 15, 60, 58, 219, 0, 50)
racket_x = 1
racket_y = 1
game = True

move_right = False
move_left = False
 
racket_speed = 6
 
speed_x = 10
speed_y = 10
ball = Ball(326, 200, 50, 50, 'ball.png')


racket = Picture('52.jpg', racket_x, racket_y, 1, 1)
 
start_x = 5
start_y = 5
 
count = 9
monsters = []

font.init()
font = font.Font(None, 50)
score_num = 0
score_num2 = 0
run = True 
while run:
    score = font.render(
                'Счет: ' + str(score_num), True, (0, 0, 0)
            )
    score2 = font.render(
                'Счет: ' + str(score_num2), True, (0, 0, 0)
            )
    win = font.render(
                'Победил игрок!', True, (255, 0, 0)
            )
    lose = font.render(
                'Победил робот!', True, (255, 0, 0)
            )
    restart = font.render(
                'Если хотите начать заново, нажмите  - r', True, (255, 0, 0)
            )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
    if game:

        if move_left:
           racket.rect.x -= racket_speed
        if move_right:
            racket.rect.x += racket_speed
 

        ball.rect.x += speed_x
        ball.rect.y += speed_y
 

        if ball.rect.y < 0 or ball.rect.y > width_size - 120:
            speed_y *= -1
        if ball.rect.x < 0:
            speed_x *= -1
            score_num2 += 1
            ball.rect.x = 326
            ball.rect.y = 200 

        if wall2.colliderect(ball) or wall1.colliderect(ball):
            speed_x *= -1

        if ball.rect.x > len_size - 50:
            score_num += 1
            speed_x *= -1
            ball.rect.x = 326
            ball.rect.y = 200 
    
    window.blit(image, (0, 0))
    window.blit(score, (10, 20))
    window.blit(score2, (570, 20))
    ball.draw()
    ball.update()
    wall1.draw_wall()
    wall2.draw_wall()
    wall1.update()
    wall2.update()

    if score_num >= 3:
        window.blit(win, (326, 200))
        game = False
        window.blit(restart, (15, 320))
        keys = key.get_pressed()
        if keys[K_r]:
            score_num = 0
            score_num2 = 0
            game = True


    if score_num2 >=3:
        window.blit(lose, (326, 200))
        game = False
        window.blit(restart, (15, 320))
        keys = key.get_pressed()
        if keys[K_r]:
            score_num = 0
            score_num2 = 0
            game = True

    pygame.display.update()
    clock.tick(40)
