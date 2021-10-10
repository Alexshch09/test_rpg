import pygame
from items import *
from colors import *
from config import *

f1 = pygame.font.Font(None, 16)
def small_magic_shop_render():
    object1 = f1.render(small_health_potion["name"], True, BLACK)
    object2 = f1.render(medium_health_potion["name"], True, BLACK)
    object3 = f1.render(small_mana_potion["name"], True, BLACK)
    object4 = f1.render(teleport["name"], True, BLACK)
    price1 = f1.render(small_health_potion["price"]+" Gold", True, BLACK)
    price2 = f1.render(medium_health_potion["price"]+" Gold", True, BLACK)
    price3 = f1.render(small_mana_potion["price"]+" Gold", True, BLACK)
    price4 = f1.render(teleport["price"]+" Gold", True, BLACK)
    screen.blit(shop_menu, (0,0,0,0))
    screen.blit(small_health_potion["image"], (128,128))
    screen.blit(object1, (102,175,0,0))
    screen.blit(price1, (140,200,0,0))
    screen.blit(medium_health_potion["image"], (310,128,0,0))
    screen.blit(object2, (286,175,0,0))
    screen.blit(price2, (324,200,0,0))
    screen.blit(small_mana_potion["image"], (128,310,0,0))
    screen.blit(object3, (102,357,0,0))
    screen.blit(price3, (140,382,0,0))
    screen.blit(teleport["image"], (310,310,0,0))
    screen.blit(object4, (286,357,0,0))
    screen.blit(price4, (324,382,0,0))

def inventory_render():
    screen.blit(shop_menu, (0,0,0,0))
