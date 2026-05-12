import pygame
 

pygame.init()

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

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def update(self):
        keys = key.get_pressed()
        if (keys[K_w] or keys[K_LEFT]) and self.rect.x > 5:
            self.rect.x -= self.speed
        if (keys[K_s] or  keys[K_RIGHT])  and self.rect.x < 700 - 70:
            self.rect.x += self.speed
 
back = (200, 255, 255)
window = pygame.display.set_mode((700, 500))
image = pygame.transform.scale(pygame.image.load('52.jpg'), (700, 500))
#window.fill(image)
clock = pygame.time.Clock()
 
racket_x = 1
racket_y = 5
game = True

move_right = False
move_left = False
 
racket_speed = 6
 
speed_x = 4
speed_y = 4
 
ball = Picture('ball.png', 160, 200, 5, 5)

racket = Picture('52.jpg', racket_x, racket_y, 7, 5)
 
start_x = 5
start_y = 5
 
count = 9
monsters = []

# for i in range(3):
#     x = start_x + (27.5 * i) 
#     y = start_y + (55 * i)
#     for j in range(count):
#         monster = Picture('enemy.png', x, y, 50, 50)
#         monsters.append(monster)
#         x += 55
#     count -= 1
 
while game:

    ball.fill()
    #racket.fill()
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
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
 

    if ball.colliderect(racket.rect):
        speed_y *= -1

    # if ball.rect.y > (racket_y + 20):
    #     game_end = Label(150, 150, 50, 50, back)
    #     game_end.set_text('YOU LOSE!', 60, (255, 0, 0))
    #     game_end.draw(10,10)
    #     game = False
 
    # if len(monsters) == 0:
    #     game_end = Label(150, 150, 50, 50, back)
    #     game_end.set_text('YOU WIN!', 60, (0, 200, 0))
    #     game_end.draw(10,10)
    #     game = False
 
    # for monster in monsters:
    #     monster.draw()
    #     if monster.colliderect(ball.rect):
    #         monsters.remove(monster)
    #         monster.fill()
    #         speed_y *= -1 
    window.blit(image, (0, 0))
    ball.draw()
    #racket.draw()
    pygame.display.update()
    clock.tick(40)
