

from pygame import *

back = (100, 155, 255)
win_width = 600
win_height = 500
win = display.set_mode((win_width, win_height))
win.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y	
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.r

racked1= Player('__.png', 30, 200, 4, 50, 150)
racked2= Player('__.png', 520, 200, 4, 50, 150)
ball = GameSprite('----,png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('Player 1 lose', True, (180, 0, 0))
lose2 = font.render('Player 2 lose', True, (180, 0, 0))

speed_x = 3
speed_x = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        racked1.update_l()
        racked2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racked1, ball) or sprite.collide_rect(racked2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True
    
        racked1.reset()
        racked2.reset()
        ball.reset()
    
    display.update()
    clock.tick(FPS)

