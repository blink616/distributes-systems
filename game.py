#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from player import Player
from environment import *
from flag import *
from enemies import *
from flag import *
from environment import *
import tkinter
from tkinter import messagebox
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)

#key variables
maptype = 'hard1'
playerCharacter = "graphic/character6.png"
playerWalk = "graphic/character6Walk.png"
playerExplosion = "graphic/explosion6.png"

class Game(object):
    def __init__(self):
        self.font = pygame.font.Font(None,40)

        #defining menus
        self.game_over = True
        self.mainmenu = True
        self.single_player = False
        self.multi_player = False
        self.character = False
        self.scoreboard = False

        # Create the variable for the score
        self.score = 0
        # Create the font for displaying the score on the screen
        self.font = pygame.font.Font(None,35)

        # Create the menu of the game
        self.menu = Menu(("Single Player","Multiplayer","Exit"),font_color = WHITE,font_size=60)
        # Create the single player game menu of the game
        self.single_menu = Menu(("Death Match","Clear Map","Score Board", "Back"),font_color = WHITE,font_size=60)
        # Create the multiplayer game menu of the game
        self.multi_menu = Menu(("Death Match","Clear Map","Back"),font_color = WHITE,font_size=60)
        # Create the scorecard of the game
        self.score_menu = Menu(("Score Board","Back"),font_color = WHITE,font_size=60)

        # Create the player
        self.player = Player(32,128,playerCharacter, playerWalk, playerExplosion)
        # Create the blocks that will set the paths where the player can go
        self.up_blocks = pygame.sprite.Group()
        self.down_blocks = pygame.sprite.Group()
        self.left_blocks = pygame.sprite.Group()
        self.right_blocks = pygame.sprite.Group()
        # Create a group for the dots on the screen
        self.dots_group = pygame.sprite.Group()
        # Set the enviroment:
        for i,row in enumerate(enviroment(maptype)):
            for j,item in enumerate(row):
                if item == 1 or item == 4 or item == 8 or item == 9:
                    self.up_blocks.add(Block(j*32+8,i*32+8,BLACK,16,16))
                if item == 2 or item == 6 or item == 8 or item == 10:
                    self.left_blocks.add(Block(j*32+8,i*32+8,BLACK,16,16))
                if item == 1 or item == 5 or item == 10 or item == 11:
                    self.down_blocks.add(Block(j*32+8,i*32+8,BLACK,16,16))
                if item == 2 or item == 7 or item == 9 or item == 11:
                    self.right_blocks.add(Block(j*32+8,i*32+8,BLACK,16,16))
        # Create the enemies
        self.enemies = pygame.sprite.Group()
        self.enemies.add(Enemy(288,67,0,2,"graphic/character1.png","graphic/character1Walk.png",maptype))
        self.enemies.add(Enemy(288,320,0,-2,"graphic/character2.png","graphic/character2Walk.png",maptype))
        self.enemies.add(Enemy(544,64,0,2,"graphic/character3.png","graphic/character3Walk.png",maptype))
        self.enemies.add(Enemy(32,224,0,2,"graphic/character4.png","graphic/character4Walk.png",maptype))
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
            self.single_menu.event_handler(event)
            self.multi_menu.event_handler(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:

                    #on main menu
                    if self.game_over and self.mainmenu:
                        if self.menu.state == 0:
                            # ---- START SINGLE PLAYER------
                            self.__init__()
                            self.single_player = True
                            self.mainmenu = False
                        elif self.menu.state == 1:
                            # ---- START MULTI PLAYER------
                            self.__init__()
                            self.multi_player = True
                            self.mainmenu = False
                        elif self.menu.state == 2:
                            # --- EXIT -------
                            # User clicked exit
                            return True

                    #on single player menu
                    elif self.game_over and self.single_player:
                        if self.single_menu.state == 0:
                            # ---- START DEATH MATCH-----
                            self.__init__()
                            #self.game_over = False
                        elif self.single_menu.state == 1:
                            # --- START CLEAR MAP ------
                            self.__init__()
                            self.game_over = False
                        elif self.single_menu.state == 2:
                            # --- START CLEAR MAP ------
                            self.__init__()
                            self.scoreboard = True
                        elif self.single_menu.state == 3:
                            # --- BACK -------
                            self.mainmenu = True
                            self.single_player = False

                    #on multi player menu
                    elif self.game_over and self.multi_player:
                        if self.multi_menu.state == 0:
                            # ---- START DEATH MATCH-----
                            self.__init__()
                            #self.game_over = False
                        elif self.multi_menu.state == 1:
                            # --- START CLEAR MAP ------
                            self.__init__()
                            #self.game_over = False
                        elif self.multi_menu.state == 2:
                            # --- BACK -------
                            self.mainmenu = True
                            self.multi_player = False

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
                    self.multi_menu = False

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
            self.player.update(self.up_blocks,self.down_blocks,self.left_blocks,self.right_blocks)
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
            self.mainmenu = self.player.game_over
            self.enemies.update()
            #tkMessageBox.showinfo("GAME OVER!","Final Score = "+(str)(GAME.score))    

    def display_frame(self,screen):
        # First, clear the screen to white. Don't put other drawing commands
        screen.fill(BLACK)
        # --- Drawing code should go here
        if self.game_over:
            if self.single_player:
                self.single_menu.display_frame(screen)
            elif self.multi_player:
                self.multi_menu.display_frame(screen)
            elif self.scoreboard:
                self.display_message(screen, "SCOREBOARD PAGE")
            else:
                self.menu.display_frame(screen)
        else:
            # --- Draw the game here ---
            self.up_blocks.draw(screen)
            self.down_blocks.draw(screen)
            self.left_blocks.draw(screen)
            self.right_blocks.draw(screen)
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
