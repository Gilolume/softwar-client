import random
import sys
import time

import pygame

#Color
BLUE = (0,0,200)
BLACK = (0,0,0)
#End color
#Map Texture
GROUND = (58,137,35)
PLAYER = (200,200,200)
#End Map texture

#Coord
MAP_SIZE = 20
POS_X = 0
POS_Y = 90
TILE_SIZE = 20 #Toujours egal a player_size -> juste nom plus evident 
LOOKING = 0 # (left = 0, up = 1, right = 2, down = 3)
#End Coord

def generate_map(map_size):
    tilemap = []
    for row in range(map_size):
        new_row = []
        for column in range(map_size):
            new_row.append(GROUND)
        tilemap.append(new_row)
    return tilemap

def init_player(map_size, pos_x, pos_y):
    

pygame.init()
tilemap = generate_map(MAP_SIZE)
DISPLAY = pygame.display.set_mode((MAP_SIZE*TILE_SIZE,MAP_SIZE*TILE_SIZE))
PLAYER_TEXTURE = pygame.image.load("perso_mini.png")
clock = pygame.time.Clock()
gameRun = True
##display.fill(BLACK)
while gameRun:


        for row in range(MAP_SIZE):
            for column in range(MAP_SIZE):
                pygame.draw.rect(DISPLAY, tilemap[row][column], (column*TILE_SIZE, row*TILE_SIZE, TILE_SIZE, TILE_SIZE))
        #player = pygame.transform.rotate(image_player, direction)
        #display.blit(player, (pos_x, pos_y))
        pygame.display.update()
        clock.tick(15)
