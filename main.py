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
GROUND = (0, 0, 0)
#End Map texture

#Coord
TILE_SIZE = 50 #Toujours egal a player_size -> juste nom plus evident 
LOOKING = 0 # (left = 0, up = 1, right = 2, down = 3)
#End Coord

def convertToJson(notification):
    return json.loads(notification)

def getOrientation(looking):
    #left = 0, up = 1, right = 2, down = 3
    if looking == 0:
        return 90
    elif looking == 1:
        return 0
    elif looking == 2:
        return 270
    else:
        return 180

def generateMap(map_size):
    tile_map = []
    for row in range(map_size):
        new_row = []
        for column in range(map_size):
            new_row.append({"type": "ground", "color":GROUND})
        tile_map.append(new_row)
    return tile_map

def insertPlayers(tile_map, players):
    for player in players:
        tile_map[player['x'] - 1][player['y'] - 1] = {"type": "player", "data":player}
    return tile_map

def insertEnergyCells(tile_map, energy_cells):
    for energy_cell in energy_cells:
        tile_map[energy_cell['x'] - 1][energy_cell['y'] - 1] = {"type": "energy_cell", "data":energy_cell}
    return tile_map

def drawMap(pygame, data):
    map_size = data['map_size']
    tile_map = generateMap(map_size)
    tile_map = insertPlayers(tile_map, data['players'])
    tile_map = insertEnergyCells(tile_map, data['energy_cells'])
    display = pygame.display.set_mode((map_size*TILE_SIZE,map_size*TILE_SIZE))
    for row in range(map_size):
        for column in range(map_size):
            if tile_map[row][column]['type'] == "ground":
                pygame.draw.rect(display, tile_map[row][column]['color'], (column*TILE_SIZE, row*TILE_SIZE, TILE_SIZE, TILE_SIZE))
            elif tile_map[row][column]['type'] == "player":
                playerOriented = pygame.transform.rotate(PLAYER, getOrientation(tile_map[row][column]['data']['looking']))
                display.blit(playerOriented, (column*TILE_SIZE, row*TILE_SIZE))
            else:
                display.blit(ENERGY_CELL, (column*TILE_SIZE, row*TILE_SIZE))

def drawMessageStart(pygame):
    display = pygame.display.set_mode((500,500))
    myFont = pygame.font.SysFont("Impact", 50)
    gameStartInfo = myFont.render("Game start", 1, (255,255,255))
    display.blit(gameStartInfo, (160, 200))

def drawMessageEnd(pygame):
    #display = pygame.display.set_mode((500,500))
    display = pygame.display.get_surface()
    myFont = pygame.font.SysFont("Impact", 50)
    gameStartInfo = myFont.render("Game End", 1, (255,255,255))
    display.blit(gameStartInfo, (160, 200))

pygame.init()
PLAYER = pygame.image.load("bunny50.png")
ENERGY_CELL = pygame.image.load("energy_max50.png")
clock = pygame.time.Clock()
socket = myZmqFunc.connectToPubServer("12345")
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    notification = convertToJson(myZmqFunc.getNotification(socket))
    print(notification['notification_type'])
    if notification['notification_type'] == 10:
        drawMap(pygame, notification['data'])
    elif notification['notification_type'] == 1:
        print("Enter elif type 1")
        drawMessageStart(pygame)
    elif notification['notification_type'] == 2:
        print("Un seul client est encore en vie")
        drawMessageEnd(pygame)
    elif notification['notification_type'] == 3:
        print("Mort d'un client")
    elif notification['notification_type'] == 4:
        print("Victoire d'un client")

 
    pygame.display.update()
    #clock.tick(15)
