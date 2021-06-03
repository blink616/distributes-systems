#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from player import Player
from environment import *
from scoreboard import *
from flag import *
from enemies import *
from environment import *
from mapSelect import *
from characterSelect import *
from setConnection import *
from menu import *
from bullet import *
import tkinter
from tkinter import messagebox
import time
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
YELLOW=(255,255,0)
pygame.init()
delay_time = 1000  # 8 seconds
pause_time = 8000 # 6 seconds
bullet_event = pygame.USEREVENT + 1
pygame.time.set_timer(bullet_event, delay_time)


class Game(object):
    
    #CHANGE
    playerID = 0
    maptype = 'map3'
    playerName = "playername"
    playerCharacter = "graphic/character6.png"
    playerWalk = "graphic/character6Walk.png"
    playerExplosion = "graphic/explosion6.png"
    port = 11222
    serverurl = "127.0.0.1"
    
    def __init__(self):
        self.font = pygame.font.Font(None,40)

        #defining menus
        self.mainmenu = True
        self.deathMatch_gameover = True
        self.clearMap_gameover = True
        self.single_player = False
        self.multi_player = False
        self.character = False
        self.scoreboard = False
        self.mapSingle = False
        self.mapMulti = False
  
        self.start_time = 0
        self.end_time = 0

        # Create the variable for the score
        self.score = 0
        self.death = 0
        self.no_shots = 0

        # Create the font for displaying the score on the screen
        self.font = pygame.font.Font(None,35)

        #create map select and character select
        self.mapSelect = mapSelect()
        self.characterSelect = characterSelect()

        # Create the menu of the game
        self.menu = Menu(("Single Player","Multiplayer","Select Player","Exit"),font_color = WHITE,font_size=60)
        # Create the single player game menu of the game
        self.single_menu = Menu(("Death Match","Clear Map","Select Map","Score Board", "Back"),font_color = WHITE,font_size=60)
        # Create the multiplayer game menu of the game
        self.multi_menu = Menu(("Death Match","Clear Map","Select Map","Back"),font_color = WHITE,font_size=60)
        # Create the scorecard of the game
        self.score_menu = Scoreboard(("Score Board","Back"),select_color = BLUE, font_color = WHITE,font_size=30)

        

        # Create the player
        self.player = Player(32,194,self.playerCharacter, self.playerWalk, self.playerExplosion)
        # Create the blocks that will set the paths where the player can go
        self.up_blocks = pygame.sprite.Group()
        self.down_blocks = pygame.sprite.Group()
        self.left_blocks = pygame.sprite.Group()
        self.right_blocks = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.enemy_bullet_group = pygame.sprite.Group()
        # Create a group for the dots on the screen
        self.dots_group = pygame.sprite.Group()
        # Set the enviroment:
        for i,row in enumerate(enviroment(self.maptype)):
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
        self.blocks_array = [self.up_blocks, self.down_blocks, self.left_blocks, self.right_blocks]
        self.enemiesClearMap = pygame.sprite.Group()
        self.enemiesClearMap.add(Enemy(288,67,0,2,"graphic/character1.png","graphic/character1Walk.png",self.maptype, "clearmap", self.blocks_array))
        self.enemiesClearMap.add(Enemy(288,320,0,-2,"graphic/character2.png","graphic/character2Walk.png",self.maptype, "clearmap", self.blocks_array))
        self.enemiesClearMap.add(Enemy(544,64,0,2,"graphic/character3.png","graphic/character3Walk.png",self.maptype, "clearmap", self.blocks_array))
        self.enemiesClearMap.add(Enemy(32,267,0,2,"graphic/character4.png","graphic/character4Walk.png",self.maptype, "clearmap", self.blocks_array))
        self.enemiesClearMap.add(Enemy(162,64,2,0,"graphic/character1.png","graphic/character1Walk.png",self.maptype, "clearmap", self.blocks_array))
        self.enemiesClearMap.add(Enemy(450,64,-2,0,"graphic/character2.png","graphic/character2Walk.png",self.maptype, "clearmap", self.blocks_array))
        self.enemiesClearMap.add(Enemy(642,448,2,0,"graphic/character3.png","graphic/character3Walk.png",self.maptype, "clearmap", self.blocks_array))
        self.enemiesClearMap.add(Enemy(450,320,2,0,"graphic/character5.png","graphic/character5Walk.png",self.maptype,"clearmap", self.blocks_array))
        self.enemiesDeathMatch = pygame.sprite.Group()
        self.enemiesDeathMatch.add(Enemy(288,67,0,2,"graphic/character1.png","graphic/character1Walk.png",self.maptype, "deathmatch", self.blocks_array))
        self.enemiesDeathMatch.add(Enemy(288,320,0,-2,"graphic/character2.png","graphic/character2Walk.png",self.maptype, "deathmatch", self.blocks_array))
        self.enemiesDeathMatch.add(Enemy(544,64,0,2,"graphic/character3.png","graphic/character3Walk.png",self.maptype, "deathmatch", self.blocks_array))
        self.enemiesDeathMatch.add(Enemy(32,267,0,2,"graphic/character4.png","graphic/character4Walk.png",self.maptype, "deathmatch", self.blocks_array))
        self.enemiesDeathMatch.add(Enemy(162,64,2,0,"graphic/character1.png","graphic/character1Walk.png",self.maptype, "deathmatch", self.blocks_array))
        self.enemiesDeathMatch.add(Enemy(450,64,-2,0,"graphic/character2.png","graphic/character2Walk.png",self.maptype, "deathmatch", self.blocks_array))
        self.enemiesDeathMatch.add(Enemy(642,448,2,0,"graphic/character3.png","graphic/character3Walk.png",self.maptype, "deathmatch", self.blocks_array))
        self.enemiesDeathMatch.add(Enemy(450,320,2,0,"graphic/character5.png","graphic/character5Walk.png",self.maptype,"deathmatch", self.blocks_array))
        
        # Add the dots inside the game
        for i, row in enumerate(enviroment(self.maptype)):
            for j, item in enumerate(row):
                if item != 0:
                    self.dots_group.add(Flag(j*32+12,i*32+12,WHITE,8,8))

        # Load the sound effects
        self.pacman_sound = pygame.mixer.Sound("sound/pacman_sound.ogg")
        self.game_over_sound = pygame.mixer.Sound("sound/game_over_sound.ogg")


    def process_events(self,screen):
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                return True
            
            if (self.clearMap_gameover and self.deathMatch_gameover) and self.scoreboard:
                self.score_menu.event_handler(event)
            elif (self.clearMap_gameover and self.deathMatch_gameover) and self.character:
                self.characterSelect.event_handler(event,screen)
            elif (self.clearMap_gameover and self.deathMatch_gameover) and self.mapSingle:
                self.mapSelect.event_handler(event,screen)
                print("event is handled")
            elif (self.clearMap_gameover and self.deathMatch_gameover) and self.single_player:
                self.single_menu.event_handler(event)
            elif (self.clearMap_gameover and self.deathMatch_gameover) and self.multi_player:
                self.multi_menu.event_handler(event)

            elif (self.clearMap_gameover and self.deathMatch_gameover) and self.mainmenu:
                self.menu.event_handler(event)


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:

                    #on main menu
                    if (self.clearMap_gameover and self.deathMatch_gameover) and self.mainmenu:
                        if self.menu.state == 0:
                            # ---- START SINGLE PLAYER------
                            self.__init__()
                            self.single_player = True
                            self.mainmenu = False
                        elif self.menu.state == 1:
                            # ---- START MULTI PLAYER------
                            self.__init__()
                            self.playerID = input("Enter ID:")
                            self.setConnection = setConnection(self.playerID, self.port, self.serverurl)
                            self.multi_player = True
                            self.mainmenu = False
                        elif self.menu.state == 2:
                            self.__init__()

                            self.character = True
                            self.mainmenu = False

                        elif self.menu.state == 3:
                            # --- EXIT -------
                            # User clicked exit
                            return True

                    #on single player menu
                    elif (self.clearMap_gameover and self.deathMatch_gameover) and self.single_player:


                        if self.single_menu.state == 0:
                            # ---- START DEATH MATCH-----
                            self.__init__()
                            self.deathMatch_gameover = False
                            self.single_player = False
                            

                        elif self.single_menu.state == 1:
                            # --- START CLEAR MAP ------
                            self.__init__()
                            self.clearMap_gameover = False
                            self.single_player = False
                            self.start_time = time.time()

                        elif self.single_menu.state == 2:
                            # --- SELECT MAP ---
                            self.__init__()
                            self.mapSingle=True
                            self.single_player=False

                        elif self.single_menu.state == 3:
                            # --- SCORE BOARD ------
                            self.__init__()
                            self.scoreboard = True
                            self.single_player = False

                        elif self.single_menu.state == 4:
                            # --- BACK -------
                            self.__init__()
                            self.mainmenu = True
                            self.single_player = False

                    #on score menu
                    elif (self.clearMap_gameover and self.deathMatch_gameover) and self.scoreboard:
                        if self.score_menu.state == 0:
                            self.__init__()
                            self.single_player = True
                            self.scoreboard = False
                            self.mainmenu = False

                    #on multi player menu
                    elif (self.clearMap_gameover and self.deathMatch_gameover) and self.multi_player:
                        if self.multi_menu.state == 0:
                            # ---- START DEATH MATCH-----
                            self.__init__()
                            self.mainmenu = True
                            self.multi_player = False
                        elif self.multi_menu.state == 1:
                            # --- START CLEAR MAP ------
                            self.__init__()
                            self.mainmenu = True
                            self.multi_player = False
                        elif self.multi_menu.state == 2:
                            # --- SELECT MAP ---
                            self.__init__()
                            self.mainmenu = True
                            self.multi_player = False

                        elif self.multi_menu.state == 2:
                            # --- BACK -------
                            self.__init__()
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
                elif event.key == pygame.K_RCTRL:
                    self.bullet_group.add(self.player.create_bullet())
                
                elif event.key == pygame.K_ESCAPE:
                    self.deathMatch_gameover = True
                    self.clearMap_gameover = True
                    self.mainmenu = True
                    self.multi_player = False
                    self.single_player = False
                    self.scoreboard = False
                    self.character = False
                    self.mapSingle = False

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.stop_move_right()
                elif event.key == pygame.K_LEFT:
                    self.player.stop_move_left()
                elif event.key == pygame.K_UP:
                    self.player.stop_move_up()
                elif event.key == pygame.K_DOWN:
                    self.player.stop_move_down()

            elif event.type == bullet_event:
                     for enemy in self.enemiesDeathMatch:
                         self.enemy_bullet_group.add(enemy.create_bullet())
                         if self.no_shots == 0:
                             pygame.time.set_timer(bullet_event, delay_time)
                         self.no_shots += 1
                         if self.no_shots == 5:
                            pygame.time.set_timer(bullet_event, pause_time)
                            self.no_shots = 0   

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.player.explosion = True
                    
        return False

    def run_logic(self):
        if not self.clearMap_gameover:
            self.player.update(self.up_blocks,self.down_blocks,self.left_blocks,self.right_blocks)
            block_hit_list = pygame.sprite.spritecollide(self.player,self.dots_group,True)
            # When the block_hit_list contains one sprite that means that player hit a dot
            if len(block_hit_list) > 0:
                # Here will be the sound effect
                self.pacman_sound.play()
                self.score += 1
            block_hit_list = pygame.sprite.spritecollide(self.player,self.enemiesClearMap,True)
            if len(block_hit_list) > 0:
                self.player.explosion = True
                self.game_over_sound.play()
            self.clearMap_gameover = self.player.game_over
            self.scoreboard = self.player.game_over
            self.enemiesClearMap.update()

            #if this event kills player and we move to scorescreen
            if self.player.game_over == True:
                self.end_time = time.time()
                self.score_menu.newscore(self.playerName,"clearmap", self.score, self.start_time, self.end_time)
        
        elif not self.deathMatch_gameover:
            self.player.update(self.up_blocks,self.down_blocks,self.left_blocks,self.right_blocks)
            block_hit_list = pygame.sprite.groupcollide(self.enemiesDeathMatch,self.bullet_group,True, True, collided = None)
            # When the block_hit_list contains one sprite that means that player hit a dot
            if len(block_hit_list) > 0:
                for enemy in block_hit_list:
                    self.enemiesDeathMatch.add(Enemy(enemy.position[0], enemy.position[1], enemy.position[2], enemy.position[3], enemy.enemy_picture, enemy.walk, enemy.maptype, "deathmatch", self.blocks_array))
                self.score += 1
            block_hit_list = pygame.sprite.spritecollide(self.player,self.enemy_bullet_group,True)
            if len(block_hit_list) > 0:
                self.player.explosion = True
                self.player = Player(32,194,self.playerCharacter, self.playerWalk, self.playerExplosion)
                self.death += 1
                self.game_over_sound.play()
            self.deathMatch_gameover = self.player.game_over
            self.scoreboard = self.player.game_over
            self.enemiesDeathMatch.update()
            #if this event kills player and we move to scorescreen
            if self.player.game_over == True:
                self.end_time = time.time()
                self.score_menu.newscore(self.playerName,"deathmatch", self.score, self.start_time, self.end_time)
          

    def display_frame(self,screen):
        # First, clear the screen to white. Don't put other drawing commands
        screen.fill(BLACK)
        # --- Drawing code should go here
        if self.clearMap_gameover and self.deathMatch_gameover:
            if self.single_player:
                print("this is single screen")
                self.single_menu.display_frame(screen)
            elif self.multi_player:
                self.multi_menu.display_frame(screen)

            elif self.mapSingle:
                temp = self.mapSelect.display_frame(screen)
                print("game", temp)
                if temp[0] != "path":
                    self.maptype = "map"+ temp[0]
                if temp[1] == "done":
                    self.mapSingle= False
                    self.single_player= True

            elif self.character:
                temp = self.characterSelect.display_frame(screen)
                self.playerCharacter = "graphic/character"+ temp[0] +".png" 
                self.playerWalk = "graphic/character"+ temp[0] +"Walk.png" 
                self.playerExplosion = "graphic/explosion"+ temp[0] +".png" 
                if temp[1] == "done":
                    self.character = False
                    self.mainmenu = True
            
            elif self.scoreboard:
                self.score_menu.display_frame(screen)
            else:
                self.menu.display_frame(screen)
        else:
            # --- Draw the game here ---
            self.up_blocks.draw(screen)
            self.down_blocks.draw(screen)
            self.left_blocks.draw(screen)
            self.right_blocks.draw(screen)
            draw_enviroment(screen, self.maptype)
            if not self.clearMap_gameover:
                self.dots_group.draw(screen)
            if not self.clearMap_gameover:
                self.enemiesClearMap.draw(screen)
            if not self.deathMatch_gameover:
                self.enemiesDeathMatch.draw(screen)
                self.bullet_group.draw(screen)
                self.bullet_group.update()
                self.enemy_bullet_group.draw(screen)
                self.enemy_bullet_group.update()

            screen.blit(self.player.image,self.player.rect)
            #text=self.font.render("Score: "+(str)(self.score), 1,self.RED)
            #screen.blit(text, (30, 650))
            # Render the text for the score
            if not self.clearMap_gameover:
                text = self.font.render("Flags: " + str(self.score),True,GREEN)
            if not self.deathMatch_gameover:
                text = self.font.render("Kills: " + str(self.score) + " Deaths: " + str(self.death), True, GREEN)
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
