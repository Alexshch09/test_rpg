import pygame
import time
from sprites import *
from config import *
from colors import *
from data import *
from maps import *

x=0
y=0
current_map_id=1
map_list = [
[start_village, start_village_tiles],
[forest1, forest1_tiles]
]

# Создаем игру и окно
pygame.init()
pygame.font.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

def draw_map(id):
    map=map_list[id][0]
    tiles=map_list[id][1]
    for x in range(8):
        for y in range(8):
            sprite_to_draw=tiles[map[y][x]]
            screen.blit(sprite_to_draw, sprite_to_draw.get_rect(bottomright=(64+x*64, 64+y*64)))

# Цикл игры
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if (player.rect.x>0):
            for a in range(64):
                draw_map(current_map_id)
                player.rect.x -= 1
                all_sprites.draw(screen)
                pygame.display.flip()
                time.sleep(0.01)
    elif keys[pygame.K_RIGHT]:
        if (player.rect.x<448):
            for a in range(64):
                draw_map(current_map_id)
                player.rect.x += 1
                all_sprites.draw(screen)
                pygame.display.flip()
                time.sleep(0.01)
    elif keys[pygame.K_DOWN]:
        if (player.rect.y<448):
            for a in range(64):
                draw_map(current_map_id)
                player.rect.y += 1
                all_sprites.draw(screen)
                pygame.display.flip()
                time.sleep(0.01)
    elif keys[pygame.K_UP]:
        if (player.rect.y>0):
            for a in range(64):
                draw_map(current_map_id)
                player.rect.y -= 1
                all_sprites.draw(screen)
                pygame.display.flip()
                time.sleep(0.01)

    screen.fill(BLACK)
    draw_map(current_map_id)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
