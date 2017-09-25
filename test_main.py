import time
import random
import sys
import pygame

#import ui as ui
import testZMQ

#Color
RED = (200,0,0)
GREEN = (0,200,0)
BRIGHT_RED = (255,0,0)
BRIGHT_GREEN = (0,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
#End color

#Pos
pos_x = 0
pos_y = 90
#direction 0/180/90/170
direction = 0
player_size = 10
#End pos

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(display, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(display, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    display.blit(textSurf, textRect)

def quitgame():
	pygame.quit()
	quit()

def callserver():
	testZMQ.zmqTry()



def exec_forward():
    if send_forward() == True:
        if direction == 0:
            return pos_y - player_size
        elif direction == 180:
            return pos_y + player_size
        elif direction == 90:
            return pos_x - player_size
        elif direction == 270:
            return pos_x + player_size
def exec_backward():
    if send_backward() == True:
        if direction == 0:
            return pos_y + player_size
        elif direction == 180:
            return pos_y - player_size
        elif direction == 90:
            return pos_x + player_size
        elif direction == 270:
            return pos_x - player_size
def exec_leftwd():
    if send_leftwd() == True:
        if direction == 0:
            return 90
        elif direction == 180:
            return 270
        elif direction == 90:
            return 180
        elif direction == 270:
            return 0
def exec_rightwd():
    if send_rightwd() == True:
        if direction == 0:
            return 270
        elif direction == 180:
            return 90
        elif direction == 90:
            return 0
        elif direction == 270:
            return 180

def send_forward():
    time.sleep(.500)
    #Pas true ou false mais recup directement le json avec les infos > le parser > et mettre à jour la position par rapport au json
    return True
def send_backward():
    time.sleep(.500)
    return True
def send_leftwd():
    time.sleep(.500)
    return True
def send_rightwd():
    time.sleep(.500)
    return True


pygame.init()
display = pygame.display.set_mode((100,100))
image_player = pygame.image.load("perso_mini.png")
clock = pygame.time.Clock()
gameExit = False
while not gameExit:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    if direction == 0 or direction == 180:
                        pos_y = exec_forward()
                    else:
                        pos_x = exec_forward()
                if event.key == pygame.K_DOWN:
                    if direction == 0 or direction == 180:
                        pos_y = exec_backward()
                    else:
                        pos_x = exec_backward()
                if event.key == pygame.K_LEFT:
                    direction = exec_leftwd()
                if event.key == pygame.K_RIGHT:
                    direction = exec_rightwd()
                
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        display.fill(WHITE)


        #
        #C'est dans cette boucle qu'on parse les json pour déterminer la position de tout les joueurs et toutes les capsules
        #d'énergie. et dans un for placer après l'affichage des élement de la map on va asombrire le terrain par rapport au champ 
        #de vision
        #

        #button("Call server",150,450,100,50,GREEN,BRIGHT_GREEN,callserver)
        #button("Quit",550,450,100,50,RED,BRIGHT_RED,quitgame)
        player = pygame.transform.rotate(image_player, direction)
        display.blit(player, (pos_x, pos_y))
        pygame.display.update()
        clock.tick(15)