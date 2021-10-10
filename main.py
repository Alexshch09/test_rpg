import pygame
import time
from sprites import *
from config import *
from colors import *
from data import *
from maps import *
from items import *
from render import *

x=0
y=0
current_map_id=0
map_list = [
[start_village, start_village_tiles],
[forest1, forest1_tiles]
]
collide_list=[1]
state = 0
inventory=[]
items=[None, small_health_potion, medium_health_potion, small_mana_potion, teleport]

# Создаем игру и окно
pygame.display.set_caption(game_name)
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

def get_tile_id():
    id=current_map_id
    map=map_list[id][0]
    tiles=map_list[id][1]
    p_x=player.rect.x/64
    p_y=player.rect.y/64
    return map[int(p_y)][int(p_x)]

def tile_func(id):
    global current_map_id
    global state
    keys = pygame.key.get_pressed()
    if (id==2):
        player.rect.x=64
        player.rect.y=384
        current_map_id=1
    if (id==3):
        if keys[pygame.K_RETURN]:
            state=1
        if keys[pygame.K_ESCAPE]:
            state=0

def move_func():
    global state
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if (player.rect.x>0):
            if (player.rect.y<448):
                id = get_tile_id()
                p_x=player.rect.x/64
                p_y=player.rect.y/64
                map=map_list[current_map_id][0]
                if map[int(p_y)][int(p_x)-1] in collide_list:
                    pass
                else:
                    for a in range(64):
                        draw_map(current_map_id)
                        player.rect.x -= 1
                        all_sprites.draw(screen)
                        pygame.display.flip()
                        time.sleep(0.01)
    elif keys[pygame.K_RIGHT]:
        if (player.rect.x<448):
            if (player.rect.y<448):
                id = get_tile_id()
                p_x=player.rect.x/64
                p_y=player.rect.y/64
                map=map_list[current_map_id][0]
                if map[int(p_y)][int(p_x)+1] in collide_list:
                    pass
                else:
                    for a in range(64):
                        draw_map(current_map_id)
                        player.rect.x += 1
                        all_sprites.draw(screen)
                        pygame.display.flip()
                        time.sleep(0.01)
    elif keys[pygame.K_DOWN]:
        if (player.rect.y<448):
            id = get_tile_id()
            p_x=player.rect.x/64
            p_y=player.rect.y/64
            map=map_list[current_map_id][0]
            if map[int(p_y)+1][int(p_x)] in collide_list:
                pass
            else:
                for a in range(64):
                    draw_map(current_map_id)
                    player.rect.y += 1
                    all_sprites.draw(screen)
                    pygame.display.flip()
                    time.sleep(0.01)
    elif keys[pygame.K_UP]:
        if (player.rect.y>0):
            id = get_tile_id()
            p_x=player.rect.x/64
            p_y=player.rect.y/64
            map=map_list[current_map_id][0]
            if map[int(p_y)-1][int(p_x)] in collide_list:
                pass
            else:
                for a in range(64):
                    draw_map(current_map_id)
                    player.rect.y -= 1
                    all_sprites.draw(screen)
                    pygame.display.flip()
                    time.sleep(0.01)
    elif keys[pygame.K_i]:
        print("Inventory Opened")
        state=2

def small_magic_shop():
    global state
    keys = pygame.key.get_pressed()
    small_magic_shop_render()
    pygame.display.flip()
    screen.fill(BLACK)
    if keys[pygame.K_1]:
        print(small_health_potion["name"]+" куплено")
        inventory.append(int(small_health_potion["id"]))
        print(inventory)
        state=0
    if keys[pygame.K_2]:
        print(medium_health_potion["name"]+" куплено")
        inventory.append(int(medium_health_potion["id"]))
        print(inventory)
        state=0
    if keys[pygame.K_3]:
        print(small_mana_potion["name"]+" куплено")
        inventory.append(int(small_mana_potion["id"]))
        print(inventory)
        state=0
    if keys[pygame.K_4]:
        print(teleport["name"]+" куплено")
        inventory.append(int(teleport["id"]))
        print(inventory)
        state=0

def inventory_show():
    if (len(inventory)>0):
        x=50
        y=100
        for stage in range(len(inventory)):
            item_to_draw=items[inventory[stage]]
            screen.blit(item_to_draw["image"],(x,y))
            x+=50
# Цикл игры
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if (state==0):
        move_func()
        tile_func(get_tile_id())
        screen.fill(BLACK)
        draw_map(current_map_id)
        all_sprites.draw(screen)
        pygame.display.flip()
    if (state==1):
        tile_func(get_tile_id())
        small_magic_shop()
    if (state==2):
        keys = pygame.key.get_pressed()
        screen.fill(BLACK)
        inventory_render()
        inventory_show()
        pygame.display.flip()
        if keys[pygame.K_ESCAPE]:
            state=0
pygame.quit()
