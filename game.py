#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from player import Player
from environment import *
from flag import *
from enemies import *
from flag import *
from environment import *
from character import *
import tkinter
from tkinter import messagebox
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
YELLOW=(255,255,0)
 


#key variables
maptype = 'simple3'
playerCharacter = "graphic/character5.png"
playerWalk = "graphic/character5Walk.png"
playerExplosion = "graphic/explosion0.png"

class Game(object):
    def __init__(self):
        self.count=0
        self.up = 180
        self.down = 280
        self.left = 130
        self.right = 220


        self.font = pygame.font.Font(None,40)
        self.about = False
        self.character = False
        self.game_over = True
        # Create the variable for the score
        self.score = 0
        # Create the font for displaying the score on the screen
        self.font = pygame.font.Font(None,35)
        # Create the menu of the game
        self.menu = Menu(("Start","About","Select Character","Exit"),font_color = WHITE,font_size=60)
        # Create the player
        self.player = Player(32,128,playerCharacter, playerWalk, playerExplosion)
        # Create the blocks that will set the paths where the player can go
        self.horizontal_blocks = pygame.sprite.Group()
        self.vertical_blocks = pygame.sprite.Group()
        # Create a group for the dots on the screen
        self.dots_group = pygame.sprite.Group()
        # Set the enviroment:
        for i,row in enumerate(enviroment(maptype)):
            for j,item in enumerate(row):
                if item == 1:
                    self.horizontal_blocks.add(Block(j*32+8,i*32+8,BLACK,16,16))
                elif item == 2:
                    self.vertical_blocks.add(Block(j*32+8,i*32+8,BLACK,16,16))
        # Create the enemies
        self.enemies = pygame.sprite.Group()
        self.enemies.add(Enemy(290,96,0,2,"graphic/character1.png","graphic/character1Walk.png",maptype))
        self.enemies.add(Enemy(290,320,0,-2,"graphic/character2.png","graphic/character2Walk.png",maptype))
        self.enemies.add(Enemy(546,128,0,2,"graphic/character3.png","graphic/character3Walk.png",maptype))
        self.enemies.add(Enemy(33,224,0,2,"graphic/character4.png","graphic/character4Walk.png",maptype))
        self.enemies.add(Enemy(162,64,2,0,"graphic/character1.png","graphic/character1Walk.png",maptype))
        self.enemies.add(Enemy(450,64,-2,0,"graphic/character2.png","graphic/character2Walk.png",maptype))
        self.enemies.add(Enemy(642,448,2,0,"graphic/character3.png","graphic/character3Walk.png",maptype))
        self.enemies.add(Enemy(450,320,2,0,"graphic/character5.png","graphic/character5Walk.png",maptype))
        # Add the dots inside the game
        for i, row in enumerate(enviroment(maptype)):
            for j, item in enumerate(row):
                if item != 0:
                    self.dots_group.add(Flag(j*32+12,i*32+12,WHITE,8,8))

        # Load the sound effects
        self.pacman_sound = pygame.mixer.Sound("sound/pacman_sound.ogg")
        self.game_over_sound = pygame.mixer.Sound("sound/game_over_sound.ogg")


    def process_events(self):
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                return True
            self.menu.event_handler(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.game_over and not self.about and not self.character:
                        if self.menu.state == 0:
                            # ---- START ------
                            self.__init__()
                            self.game_over = False
                        elif self.menu.state == 1:
                            # --- ABOUT ------
                            self.about = True
                        elif self.menu.state == 2:
                            # --- Charcater Selection ------
                            self.character = True

                        elif self.menu.state == 3:
                            # --- EXIT -------
                            # User clicked exit
                            return True

                elif event.key == pygame.K_RIGHT:
                    self.player.move_right()

                elif event.key == pygame.K_LEFT:
                    self.player.move_left()

                elif event.key == pygame.K_UP:
                    self.player.move_up()

                elif event.key == pygame.K_DOWN:
                    self.player.move_down()
                
                elif event.key == pygame.K_ESCAPE:
                    self.game_over = True
                    self.about = False
                    self.character = False

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.stop_move_right()
                elif event.key == pygame.K_LEFT:
                    self.player.stop_move_left()
                elif event.key == pygame.K_UP:
                    self.player.stop_move_up()
                elif event.key == pygame.K_DOWN:
                    self.player.stop_move_down()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.player.explosion = True
                    
        return False

    def run_logic(self):
        if not self.game_over:
            self.player.update(self.horizontal_blocks,self.vertical_blocks)
            block_hit_list = pygame.sprite.spritecollide(self.player,self.dots_group,True)
            # When the block_hit_list contains one sprite that means that player hit a dot
            if len(block_hit_list) > 0:
                # Here will be the sound effect
                self.pacman_sound.play()
                self.score += 1
            block_hit_list = pygame.sprite.spritecollide(self.player,self.enemies,True)
            if len(block_hit_list) > 0:
                self.player.explosion = True
                self.game_over_sound.play()
            self.game_over = self.player.game_over
            self.enemies.update(self.horizontal_blocks,self.vertical_blocks)
           # tkMessageBox.showinfo("GAME OVER!","Final Score = "+(str)(GAME.score))    


    def display_frame(self,screen):
        # First, clear the screen to white. Don't put other drawing commands
        screen.fill(BLACK)
        # --- Drawing code should go here
        if self.game_over:
            if self.about:
                self.display_message(screen,"It is an arcade Game")
                #"a maze containing various dots,\n"
                #known as Pac-Dots, and four ghosts.\n"
                #"The four ghosts roam the maze, trying to kill Pac-Man.\n"
                #"If any of the ghosts hit Pac-Man, he loses a life;\n"
                #"the game is over.\n")
            elif self.character:

                #Image
                
                tt=pygame.font.Font(None,50)
                t = tt.render("Select Character",True,GREEN)
                screen.blit(t,[270,100])
                count=self.count
                left=self.left
                right=self.right
                up=self.up
                down=self.down
            
                for i in range(0,18):
                    if i<=5:
                        pygame.draw.line(screen, BLUE , [130+i*100, 180], [220+i*100,180], 2) #startpos, endpos,width
                        pygame.draw.line(screen, BLUE , [130+i*100, 280], [220+i*100,280], 2)

                        pygame.draw.line(screen, BLUE , [130+i*100, 180], [130+i*100,280], 2)
                        pygame.draw.line(screen, BLUE , [220+i*100, 180], [220+i*100,280], 2)


                        pika=  "graphic/character"+ str(i) +".png"
                        pikachu = pygame.image.load(pika).convert()
                        pikachu.set_colorkey(BLACK)
                        r = pikachu.get_rect()
                        r.topleft = (150+i*100,200)
                        screen.blit(pikachu,r)
                        #Name
                        tt=pygame.font.Font(None,20)
                        t = tt.render("Pikachu",True,GREEN)
                        screen.blit(t,[150+i*100,250])

                        pika_exp=  "graphic/explosion0.png"
                        pikachu_exp = pygame.image.load(pika_exp).convert()
                        pc = pygame.transform.chop(pygame.transform.chop(pikachu_exp, (30,0,0,0)), (30,30,pikachu_exp.get_width(),pikachu_exp.get_height()))
                        r = pc.get_rect()
                        r.topleft = (185+i*100,200)
                        screen.blit(pc,r)


                    elif i>5 and i<12:
                        pygame.draw.line(screen, BLUE , [130+(i-6)*100, 300], [220+(i-6)*100,300], 2) #startpos, endpos,width
                        pygame.draw.line(screen, BLUE , [130+(i-6)*100, 400], [220+(i-6)*100,400], 2)

                        pygame.draw.line(screen, BLUE , [130+(i-6)*100, 300], [130+(i-6)*100,400], 2)
                        pygame.draw.line(screen, BLUE , [220+(i-6)*100, 300], [220+(i-6)*100,400], 2)

                        Sonic=  "graphic/character"+ str(i) +".png"       
                        S = pygame.image.load(Sonic).convert()
                        S.set_colorkey(BLACK)
                        r = S.get_rect()
                        r.topleft = (150+(i-6)*100,320)
                        screen.blit(S,r)

                        tt=pygame.font.Font(None,20)
                        t = tt.render("Sonic",True,GREEN)
                        screen.blit(t,[150+(i-6)*100,370])

                        pc = pygame.transform.chop(pygame.transform.chop(pikachu_exp, (30,0,0,0)), (30,30,pikachu_exp.get_width(),pikachu_exp.get_height()))
                        r = pc.get_rect()
                        r.topleft = (180+(i-6)*100,320)
                        screen.blit(pc,r)
                    else:
                        pygame.draw.line(screen, BLUE , [130+(i-12)*100, 420], [220+(i-12)*100,420], 2) #startpos, endpos,width
                        pygame.draw.line(screen, BLUE , [130+(i-12)*100, 520], [220+(i-12)*100,520], 2)

                        pygame.draw.line(screen, BLUE , [130+(i-12)*100, 420], [130+(i-12)*100,520], 2)
                        pygame.draw.line(screen, BLUE , [220+(i-12)*100, 420], [220+(i-12)*100,520], 2)

                        Sonic= "graphic/character"+ str(i) +".png"       
                        S = pygame.image.load(Sonic).convert()
                        S.set_colorkey(BLACK)
                        r = S.get_rect()
                        r.topleft = (150+(i-12)*100,440)
                        screen.blit(S,r)

                        tt=pygame.font.Font(None,20)
                        t = tt.render("Blue Sonic",True,GREEN)
                        screen.blit(t,[150+(i-12)*100,490])

                        pc = pygame.transform.chop(pygame.transform.chop(pikachu_exp, (30,0,0,0)), (30,30,pikachu_exp.get_width(),pikachu_exp.get_height()))
                        r = pc.get_rect()
                        r.topleft = (180+(i-12)*100,440)
                        screen.blit(pc,r)

                
                
                
                #horizontal
                pygame.draw.line(screen, YELLOW , [self.left, self.up], [self.right,self.up], 2) #startpos, endpos,width
                pygame.draw.line(screen, YELLOW , [self.left, self.down], [self.right,self.down], 2)
                #vertical
                pygame.draw.line(screen, YELLOW , [self.left, self.up], [self.left,self.down], 2)
                pygame.draw.line(screen, YELLOW , [self.right, self.up], [self.right,self.down], 2)

                es=pygame.event.get()

                for e in es:
                    if e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_UP:
                            print("Player moved up!")
                            print(self.count)
                            pygame.draw.line(screen, BLUE , [left, up], [right,up], 2) #startpos, endpos,width
                            pygame.draw.line(screen, BLUE , [left, down], [right,down], 2)
                            #vertical
                            pygame.draw.line(screen, BLUE , [left, up], [left,down], 2)
                            pygame.draw.line(screen, BLUE , [right, up], [right,down], 2)
                            self.up=self.up-120
                            self.down=self.down-120
                            pygame.draw.line(screen, YELLOW , [left, up], [right,up], 2) #startpos, endpos,width
                            pygame.draw.line(screen, YELLOW , [left, down], [right,down], 2)

                            pygame.draw.line(screen, YELLOW , [left, up], [left,down], 2)
                            pygame.draw.line(screen, YELLOW , [right, up], [right,down], 2)
                            self.count-=6
                            print(self.count)
                            

                        elif e.key == pygame.K_RIGHT:
                            print("Player moved right!")
                            pygame.draw.line(screen, BLUE , [left, up], [right,up], 2) #startpos, endpos,width
                            pygame.draw.line(screen, BLUE , [left, down], [right,down], 2)
                            #vertical
                            pygame.draw.line(screen, BLUE , [left, up], [left,down], 2)
                            pygame.draw.line(screen, BLUE , [right, up], [right,down], 2)

                            self.left=self.left+100
                            self.right=self.right+100

                            pygame.draw.line(screen, YELLOW , [left, up], [right,up], 2) #startpos, endpos,width
                            pygame.draw.line(screen, YELLOW , [left, down], [right,down], 2)

                            pygame.draw.line(screen, YELLOW , [left, up], [left,down], 2)
                            pygame.draw.line(screen, YELLOW , [right, up], [right,down], 2)

                            self.count+=1
                            print(self.count)


                        elif e.key == pygame.K_DOWN:
                            print("Player moved down!")
                            pygame.draw.line(screen, BLUE , [left, up], [right,up], 2) #startpos, endpos,width
                            pygame.draw.line(screen, BLUE , [left, down], [right,down], 2)
                            #vertical
                            pygame.draw.line(screen, BLUE , [left, up], [left,down], 2)
                            pygame.draw.line(screen, BLUE , [right, up], [right,down], 2)
                            print(up)
                            self.up=self.up+120
                            self.down=self.down+120

                            pygame.draw.line(screen, YELLOW , [left, up], [right,up], 2) #startpos, endpos,width
                            pygame.draw.line(screen, YELLOW , [left, down], [right,down], 2)

                            pygame.draw.line(screen, YELLOW , [left, up], [left,down], 2)
                            pygame.draw.line(screen, YELLOW , [right, up], [right,down], 2)
                            self.count+=6
                            print(self.count)


                           

                        elif e.key == pygame.K_LEFT:

                            print("Player moved left!")
                            pygame.draw.line(screen, BLUE , [left, up], [right,up], 2) #startpos, endpos,width
                            pygame.draw.line(screen, BLUE , [left, down], [right,down], 2)
                            #vertical
                            pygame.draw.line(screen, BLUE , [left, up], [left,down], 2)
                            pygame.draw.line(screen, BLUE , [right, up], [right,down], 2)
                            self.left=self.left-100
                            self.right=self.right-100
                            print(left)
                            pygame.draw.line(screen, YELLOW , [left, up], [right,up], 2) #startpos, endpos,width
                            pygame.draw.line(screen, YELLOW , [left, down], [right,down], 2)

                            pygame.draw.line(screen, YELLOW , [left, up], [left,down], 2)
                            pygame.draw.line(screen, YELLOW , [right, up], [right,down], 2)

                            self.count-=1
                            print(self.count)

                        elif e.key==pygame.K_RETURN:
                            path="graphic/character"+ str(count) +".png" 
                            self.playerCharacter="graphic/character"+ str(count) +".png"
                            print(path)
                            self.character=False

               
               


            else:
                self.menu.display_frame(screen)
        else:
            # --- Draw the game here ---
            self.horizontal_blocks.draw(screen)
            self.vertical_blocks.draw(screen)
            draw_enviroment(screen, maptype)
            self.dots_group.draw(screen)
            self.enemies.draw(screen)
            screen.blit(self.player.image,self.player.rect)
            #text=self.font.render("Score: "+(str)(self.score), 1,self.RED)
            #screen.blit(text, (30, 650))
            # Render the text for the score
            text = self.font.render("Score: " + str(self.score),True,GREEN)
            # Put the text on the screen
            screen.blit(text,[120,20])
            
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    def display_message(self,screen,message,color=(255,0,0)):
        label = self.font.render(message,True,color)
        # Get the width and height of the label
        width = label.get_width()
        height = label.get_height()
        # Determine the position of the label
        posX = (SCREEN_WIDTH /2) - (width /2)
        posY = (SCREEN_HEIGHT /2) - (height /2)
        # Draw the label onto the screen
        screen.blit(label,(posX,posY))


class Menu(object):
    state = 0
    def __init__(self,items,font_color=(0,0,0),select_color=(255,0,0),ttf_font=None,font_size=25):
        self.font_color = font_color
        self.select_color = select_color
        self.items = items
        self.font = pygame.font.Font(ttf_font,font_size)
        
    def display_frame(self,screen):
        for index, item in enumerate(self.items):
            if self.state == index:
                label = self.font.render(item,True,self.select_color)
            else:
                label = self.font.render(item,True,self.font_color)
            
            width = label.get_width()
            height = label.get_height()
            
            posX = (SCREEN_WIDTH /2) - (width /2)
            # t_h: total height of text block
            t_h = len(self.items) * height
            posY = (SCREEN_HEIGHT /2) - (t_h /2) + (index * height)
            
            screen.blit(label,(posX,posY))
        
    def event_handler(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if self.state > 0:
                    self.state -= 1
            elif event.key == pygame.K_DOWN:
                if self.state < len(self.items) -1:
                    self.state += 1

    