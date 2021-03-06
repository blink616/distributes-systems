import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)


def enviroment(maptype):
    #different maps 
    if maptype == 'simple1':
        grid = ((0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
                (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
                (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
                (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
                (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0))

    elif maptype == 'simple2':
        grid = ((0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
                (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
                (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
                (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
                (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
                (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),    
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0))

    elif maptype == 'simple3':
        grid = ((0,2,0,0,0,0,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,0,0,2,0),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,0,0,2,0),
                (1,3,1,1,1,1,1,1,1,3,1,1,1,3,1,1,1,3,1,1,1,1,1,3,1),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,0,0,2,0),
                (1,3,1,1,1,1,1,1,1,3,1,1,1,3,1,1,1,3,1,1,1,1,1,3,1),    
                (0,2,0,0,0,0,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,0,0,2,0),
                (1,3,1,1,1,1,1,1,1,3,1,1,1,3,1,1,1,3,1,1,1,1,1,3,1),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,0,0,2,0),
                (1,3,1,1,1,1,1,1,1,3,1,1,1,3,1,1,1,3,1,1,1,1,1,3,1),    
                (0,2,0,0,0,0,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,0,0,2,0),
                (1,3,1,1,1,1,1,1,1,3,1,1,1,3,1,1,1,3,1,1,1,1,1,3,1),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,0,0,2,0),
                (1,3,1,1,1,1,1,1,1,3,1,1,1,3,1,1,1,3,1,1,1,1,1,3,1),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,0,0,2,0),
                (1,3,1,1,1,1,1,1,1,3,1,1,1,3,1,1,1,3,1,1,1,1,1,3,1),    
                (0,2,0,0,0,0,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,0,0,2,0),
                (1,3,1,1,1,1,1,1,1,3,1,1,1,3,1,1,1,3,1,1,1,1,1,3,1),    
                (0,2,0,0,0,0,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,0,0,2,0))

    elif maptype == 'hard1':
        grid = ((0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
                (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,4,1,3,1),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,2,0,2,0),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,8,1,11,0,2,0),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,2,0,0,0,2,0),
                (1,3,1,1,1,1,1,1,1,3,1,1,1,4,1,1,1,3,1,5,1,1,1,3,1),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,0,0,2,0),
                (0,2,0,8,1,1,1,1,1,3,1,1,1,7,0,0,0,2,0,0,0,0,0,2,0),
                (0,2,0,2,0,0,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,0,0,2,0),
                (1,7,0,10,1,1,1,1,1,3,1,1,1,5,1,1,1,5,1,1,1,1,1,3,1),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0),
                (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,4,1,1,1,1,1,3,1),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
                (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),    
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
                (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0))

    return grid

def draw_enviroment(screen,maptype):
    for i,row in enumerate(enviroment(maptype)):
        for j,item in enumerate(row):
            if item == 1: #up down
                pygame.draw.line(screen, BLUE , [j*32, i*32], [j*32+32,i*32], 1)
                pygame.draw.line(screen, BLUE , [j*32, i*32+32], [j*32+32,i*32+32], 1)
            elif item == 2: #left right
                pygame.draw.line(screen, BLUE , [j*32, i*32], [j*32,i*32+32], 1)
                pygame.draw.line(screen, BLUE , [j*32+32, i*32], [j*32+32,i*32+32],1)
            elif item == 4: #up
                pygame.draw.line(screen, BLUE , [j*32, i*32], [j*32+32,i*32], 1)
            elif item == 5: #down
                pygame.draw.line(screen, BLUE , [j*32, i*32+32], [j*32+32,i*32+32], 1)
            elif item == 6: #left
                pygame.draw.line(screen, BLUE , [j*32, i*32], [j*32,i*32+32], 1)
            elif item == 7: #right
                pygame.draw.line(screen, BLUE , [j*32+32, i*32], [j*32+32,i*32+32], 1)
            elif item == 8: #up left
                pygame.draw.line(screen, BLUE , [j*32, i*32], [j*32+32,i*32], 1)
                pygame.draw.line(screen, BLUE , [j*32, i*32], [j*32,i*32+32], 1)
            elif item == 9: #up right
                pygame.draw.line(screen, BLUE , [j*32, i*32], [j*32+32,i*32], 1)
                pygame.draw.line(screen, BLUE , [j*32+32, i*32], [j*32+32,i*32+32], 1)
            elif item == 10: #left down
                pygame.draw.line(screen, BLUE , [j*32, i*32], [j*32,i*32+32], 1)
                pygame.draw.line(screen, BLUE , [j*32, i*32+32], [j*32+32,i*32+32], 1)
            elif item == 11: #right down
                pygame.draw.line(screen, BLUE , [j*32+32, i*32], [j*32+32,i*32+32], 1)
                pygame.draw.line(screen, BLUE , [j*32, i*32+32], [j*32+32,i*32+32], 1)
                