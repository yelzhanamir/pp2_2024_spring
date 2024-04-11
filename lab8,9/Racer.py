import pygame
import sys
from pygame.locals import *
import random
import time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0

font = pygame.font.SysFont("Verdana", 30)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self, value):
        super().__init__()
        self.value = value  # The number of points that are added to the coin counter
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (self.value * 10, self.value * 10))  # Changing the size of a coin depending on its value
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

P1 = Player()

enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)

INC_SPEED = pygame.USEREVENT + 1
ENEMY_ADD = pygame.USEREVENT + 2
COIN_ADD = pygame.USEREVENT + 3
pygame.time.set_timer(INC_SPEED, 1000)
pygame.time.set_timer(ENEMY_ADD, 3000)
pygame.time.set_timer(COIN_ADD, 3000)

pygame.mixer.music.load("it.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.05)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == ENEMY_ADD:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        if event.type == COIN_ADD:
            coin_value = random.randint(1, 5)  # Generating a random value for a coin
            new_coin = Coin(coin_value)
            coins.add(new_coin)
            all_sprites.add(new_coin)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        if isinstance(entity, Player):
            entity.move()
        else:
            entity.move()

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (100, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    for coin in coins:
        if pygame.sprite.collide_rect(P1, coin):
            COIN_SCORE += coin.value  # Adding a coin value to the total coin counter
            coin.kill()

    score_text = font.render("Score: " + str(SCORE), True, BLACK)
    coin_text = font.render("Coins: " + str(COIN_SCORE), True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))
    DISPLAYSURF.blit(coin_text, (10, 40))

    pygame.display.update()
    FramePerSec.tick(FPS)
