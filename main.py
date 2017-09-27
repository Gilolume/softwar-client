import random
import sys
import time

import json
import pygame
import myZmqFunc

#Color
BLUE = (0,0,200)
BLACK = (0,0,0)
#End color
#Map Texture
GROUND = (58,137,35)
PLAYER = (236, 31, 30)
ENERGY_CELL = (255, 250, 98)
#End Map texture

#Coord
POS_X = 0
POS_Y = 90
TILE_SIZE = 40 #Toujours egal a player_size -> juste nom plus evident 
LOOKING = 0 # (left = 0, up = 1, right = 2, down = 3)
#End Coord

def convertToJson(notification):
    return json.loads(notification)

def generateMap(map_size):
    tile_map = []
    for row in range(map_size):
        new_row = []
        for column in range(map_size):
            new_row.append(GROUND)
        tile_map.append(new_row)
    return tile_map

def insertPlayers(tile_map, players):
    for player in players:
        tile_map[player['x'] - 1][player['y'] - 1] = PLAYER
    return tile_map

def insertEnergyCells(tile_map, energy_cells):
    for energy_cell in energy_cells:
        tile_map[energy_cell['x'] - 1][energy_cell['y'] - 1] = ENERGY_CELL
    return tile_map

def drawMap(pygame, data):
    map_size = data['map_size']
    tile_map = generateMap(map_size)
    tile_map = insertPlayers(tile_map, data['players'])
    tile_map = insertEnergyCells(tile_map, data['energy_cells'])
    display = pygame.display.set_mode((map_size*TILE_SIZE,map_size*TILE_SIZE))
    for row in range(map_size):
        for column in range(map_size):
            pygame.draw.rect(display, tile_map[row][column], (column*TILE_SIZE, row*TILE_SIZE, TILE_SIZE, TILE_SIZE))

pygame.init()
clock = pygame.time.Clock()
socket = myZmqFunc.connectToPubServer("12345")
run = True
while run:
    notification = convertToJson(myZmqFunc.getNotification(socket))
    if notification['notification_type'] == 0:
        drawMap(pygame, notification['data'])
        
    #for row in range(MAP_SIZE):
    #    for column in range(MAP_SIZE):
    #        pygame.draw.rect(DISPLAY, tilemap[row][column], (column*TILE_SIZE, row*TILE_SIZE, TILE_SIZE, TILE_SIZE))
    #player = pygame.transform.rotate(image_player, direction)
    #display.blit(player, (pos_x, pos_y))
    pygame.display.update()
    #clock.tick(15)
