#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from player import Player
from environment import *
from scoreboard import *
from flag import *
from enemies import *
from environment import *
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
        self.map=False

        #key variables
        self.maptype = 'hard1'
        self.playerName = "playername"
        self.playerCharacter = "graphic/character6.png"
        self.playerWalk = "graphic/character6Walk.png"
        self.playerExplosion = "graphic/explosion6.png"
        self.start_time = 0
        self.end_time = 0


        #character
        self.count=0
        self.up = 180
        self.down = 280
        self.left = 130
        self.right = 220
        self.name=['Kraken','Lynch','Mad Dog','ODoyle','Psycho','Ranger','Ratchet','Reaper','Rigs','Lightning','Fire-Bred','Iron Heart','Steel Foil','Gorgon','Baal','Azrael','Schizo','Manic']

        #map

        self.map_count=1
        self.map_up=140
        self.map_down=300
        self.map_right=380
        self.map_left=210

        # Create the variable for the score
        self.score = 0
        # Create the font for displaying the score on the screen
        self.font = pygame.font.Font(None,35)

        # Create the menu of the game
        self.menu = Menu(("Single Player","Multiplayer","Select Player","Exit"),font_color = WHITE,font_size=60)
        # Create the single player game menu of the game
        self.single_menu = Menu(("Death Match","Clear Map","Select Map","Score Board", "Back"),font_color = WHITE,font_size=60)
        # Create the multiplayer game menu of the game
        self.multi_menu = Menu(("Select Map","Death Match","Clear Map","Back"),font_color = WHITE,font_size=60)
        # Create the scorecard of the game
        self.score_menu = Scoreboard(("Score Board","Back"),select_color = BLUE, font_color = WHITE,font_size=30)

        

        # Create the player
        self.player = Player(32,194,self.playerCharacter, self.playerWalk, self.playerExplosion)
        # Create the blocks that will set the paths where the player can go
        self.up_blocks = pygame.sprite.Group()
        self.down_blocks = pygame.sprite.Group()
        self.left_blocks = pygame.sprite.Group()
        self.right_blocks = pygame.sprite.Group()
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
        self.enemies = pygame.sprite.Group()
        self.enemies.add(Enemy(288,67,0,2,"graphic/character1.png","graphic/character1Walk.png",self.maptype))
        self.enemies.add(Enemy(288,320,0,-2,"graphic/character2.png","graphic/character2Walk.png",self.maptype))
        self.enemies.add(Enemy(544,64,0,2,"graphic/character3.png","graphic/character3Walk.png",self.maptype))
        self.enemies.add(Enemy(32,267,0,2,"graphic/character4.png","graphic/character4Walk.png",self.maptype))
        self.enemies.add(Enemy(162,64,2,0,"graphic/character1.png","graphic/character1Walk.png",self.maptype))
        self.enemies.add(Enemy(450,64,-2,0,"graphic/character2.png","graphic/character2Walk.png",self.maptype))
        self.enemies.add(Enemy(642,448,2,0,"graphic/character3.png","graphic/character3Walk.png",self.maptype))
        self.enemies.add(Enemy(450,320,2,0,"graphic/character5.png","graphic/character5Walk.png",self.maptype))
        # Add the dots inside the game
        for i, row in enumerate(enviroment(self.maptype)):
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
            
            if self.game_over and self.scoreboard:
                self.score_menu.event_handler(event)
            elif self.game_over and self.single_player:
                self.single_menu.event_handler(event)
            elif self.game_over and self.multi_player:
                self.multi_menu.event_handler(event)

            elif self.game_over and not self.character:
                self.menu.event_handler(event)


            elif self.game_over and self.mainmenu:
                self.menu.event_handler(event)


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
                            self.__init__()

                            self.character = True
                            self.mainmenu = False

                        elif self.menu.state == 3:
                            # --- EXIT -------
                            # User clicked exit
                            return True

                    #on single player menu
                    elif self.game_over and self.single_player:


                        if self.single_menu.state == 0:
                            # ---- START DEATH MATCH-----
                            self.__init__()
                            #self.game_over = False
                            self.mainmenu = True
                            self.single_player = False

                        elif self.single_menu.state == 1:
                            # --- START CLEAR MAP ------
                            self.__init__()
                            self.game_over = False
                            self.single_player = False
                            self.start_time = time.time()

                        elif self.single_menu.state == 2:

                            self.__init__()

                            self.map=True
                            self.single_player=False

                        elif self.single_menu.state == 3:
                            # --- START CLEAR MAP ------
                            self.__init__()
                            self.scoreboard = True
                            self.single_player = False

                        elif self.single_menu.state == 4:
                            # --- BACK -------
                            self.__init__()
                            self.mainmenu = True
                            self.single_player = False

                    #on score menu
                    elif self.game_over and self.scoreboard:
                        if self.score_menu.state == 0:
                            self.__init__()
                            self.single_player = True
                            self.scoreboard = False
                            self.mainmenu = False

                    #on multi player menu
                    elif self.game_over and self.multi_player:

                        if self.single_menu.state == 0:

                            self.map=True
                            self.multi_player=False
                            self.mainmenu = True


                        if self.multi_menu.state == 1:
                            # ---- START DEATH MATCH-----
                            self.__init__()
                            self.mainmenu = True
                            self.multi_player = False

                        elif self.multi_menu.state == 2:
                            # --- START CLEAR MAP ------
                            self.__init__()
                            self.mainmenu = True
                            self.multi_player = False

                        elif self.multi_menu.state == 3:
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
                
                elif event.key == pygame.K_ESCAPE:
                    self.game_over = True
                    self.mainmenu = True
                    self.multi_player = False
                    self.single_player = False
                    self.character = False
                    self.map=False
                    self.scoreboard = False

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
            self.scoreboard = self.player.game_over
            self.enemies.update()

            #if this event kills player and we move to scorescreen
            if self.player.game_over == True:
                self.end_time = time.time()
                self.score_menu.newscore(self.playerName,"clearmap", self.score, self.start_time, self.end_time)
        

    def display_frame(self,screen):
        # First, clear the screen to white. Don't put other drawing commands
        screen.fill(BLACK)
        # --- Drawing code should go here
        if self.game_over:
            if self.single_player:
                self.single_menu.display_frame(screen)
            elif self.multi_player:
                self.multi_menu.display_frame(screen)

            elif self.map:

                title=pygame.font.Font(None,50)
                title = title.render("Select Map",True,GREEN)
                screen.blit(title,[300,90])

                
                for i in range(0,4):
                    if i<2:

                        pygame.draw.line(screen, BLUE , [210+i*200, 140], [380+i*200,140], 2) #startpos, endpos,width
                        pygame.draw.line(screen, BLUE , [210+i*200, 300], [380+i*200,300], 2)

                        pygame.draw.line(screen, BLUE , [210+i*200, 140], [210+i*200,300], 2)
                        pygame.draw.line(screen, BLUE , [380+i*200, 140], [380+i*200,300], 2)

                        m=  "graphic/map"+ str(i) +".png"
                        ma = pygame.image.load(m).convert()
                        ma = pygame.transform.scale(ma, (150, 150)) 
                        ma.set_colorkey(BLACK)
                        r = ma.get_rect()
                        r.topleft = (220+i*200,150)
                        screen.blit(ma,r)

                        tt=pygame.font.Font(None,30)
                        t = tt.render("Map"+str(i),True,GREEN)
                        screen.blit(t,[260+i*200,310])

                    else:

                        pygame.draw.line(screen, BLUE , [210+(i-2)*200, 340], [380+(i-2)*200,340], 2) #startpos, endpos,width
                        pygame.draw.line(screen, BLUE , [210+(i-2)*200, 500], [380+(i-2)*200,500], 2)

                        pygame.draw.line(screen, BLUE , [210+(i-2)*200, 340], [210+(i-2)*200,500], 2)
                        pygame.draw.line(screen, BLUE , [380+(i-2)*200, 340], [380+(i-2)*200,500], 2)

                        m=  "graphic/map"+ str(i) +".png"
                        ma = pygame.image.load(m).convert()
                        ma = pygame.transform.scale(ma, (150, 150)) 
                        ma.set_colorkey(BLACK)
                        r = ma.get_rect()
                        r.topleft = (220+(i-2)*200,345)
                        screen.blit(ma,r)

                        tt=pygame.font.Font(None,30)
                        t = tt.render("Map"+str(i),True,GREEN)
                        screen.blit(t,[260+(i-2)*200,510])


                map_up=self.map_up
                map_down=self.map_down
                map_right=self.map_right
                map_left=self.map_left
                map_count=self.map_count

                #horizontal
                pygame.draw.line(screen, YELLOW , [self.map_left, self.map_up], [self.map_right,self.map_up], 2) #startpos, endpos,width
                pygame.draw.line(screen, YELLOW , [self.map_left, self.map_down], [self.map_right,self.map_down], 2)
                #vertical
                pygame.draw.line(screen, YELLOW , [self.map_left, self.map_up], [self.map_left,self.map_down], 2)
                pygame.draw.line(screen, YELLOW , [self.map_right, self.map_up], [self.map_right,self.map_down], 2)


                es=pygame.event.get()
                for e in es:
                    if e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_UP:
                            print("Player moved up!")
                            print(self.count)
                            pygame.draw.line(screen, BLUE , [map_left, map_up], [map_right,map_up], 2) #startpos, endpos,width
                            pygame.draw.line(screen, BLUE , [map_left, map_down], [map_right,map_down], 2)
                            #vertical
                            pygame.draw.line(screen, BLUE , [map_left, map_up], [map_left,map_down], 2)
                            pygame.draw.line(screen, BLUE , [map_right, map_up], [map_right,map_down], 2)

                            self.map_up=self.map_up-200
                            self.map_down=self.map_down-200

                            pygame.draw.line(screen, BLUE , [map_left, map_up], [map_right,map_up], 2) #startpos, endpos,width
                            pygame.draw.line(screen, BLUE , [map_left, map_down], [map_right,map_down], 2)
                            #vertical
                            pygame.draw.line(screen, BLUE , [map_left, map_up], [map_left,map_down], 2)
                            pygame.draw.line(screen, BLUE , [map_right, map_up], [map_right,map_down], 2)
                            self.map_count-=2
                            print(self.map_count)
                            

                        elif e.key == pygame.K_RIGHT:
                            print("Player moved right!")
                            pygame.draw.line(screen, BLUE , [map_left, map_up], [map_right,map_up], 2) #startpos, endpos,width
                            pygame.draw.line(screen, BLUE , [map_left, map_down], [map_right,map_down], 2)
                            #vertical
                            pygame.draw.line(screen, BLUE , [map_left, map_up], [map_left,map_down], 2)
                            pygame.draw.line(screen, BLUE , [map_right, map_up], [map_right,map_down], 2)

                            self.map_left=self.map_left+200
                            self.map_right=self.map_right+200

                            pygame.draw.line(screen, BLUE , [map_left, map_up], [map_right,map_up], 2) #startpos, endpos,width
                            pygame.draw.line(screen, BLUE , [map_left, map_down], [map_right,map_down], 2)
                            #vertical
                            pygame.draw.line(screen, BLUE , [map_left, map_up], [map_left,map_down], 2)
                            pygame.draw.line(screen, BLUE , [map_right, map_up], [map_right,map_down], 2)

                            self.map_count+=1
                            print(self.map_count)


                        elif e.key == pygame.K_DOWN:
                            print("Player moved down!")
                            pygame.draw.line(screen, BLUE , [map_left, map_up], [map_right,map_up], 2) #startpos, endpos,width
                            pygame.draw.line(screen, BLUE , [map_left, map_down], [map_right,map_down], 2)
                            #vertical
                            pygame.draw.line(screen, BLUE , [map_left, map_up], [map_left,map_down], 2)
                            pygame.draw.line(screen, BLUE , [map_right, map_up], [map_right,map_down], 2)
                            
                            self.map_up=self.map_up+200
                            self.map_down=self.map_down+200

                            pygame.draw.line(screen, BLUE , [map_left, map_up], [map_right,map_up], 2) #startpos, endpos,width
                            pygame.draw.line(screen, BLUE , [map_left, map_down], [map_right,map_down], 2)
                            #vertical
                            pygame.draw.line(screen, BLUE , [map_left, map_up], [map_left,map_down], 2)
                            pygame.draw.line(screen, BLUE , [map_right, map_up], [map_right,map_down], 2)
                            self.map_count+=2
                            print(self.map_count)


                   

                        elif e.key == pygame.K_LEFT:

                            print("Player moved left!")
                            pygame.draw.line(screen, BLUE , [map_left, map_up], [map_right,map_up], 2) #startpos, endpos,width
                            pygame.draw.line(screen, BLUE , [map_left, map_down], [map_right,map_down], 2)
                            #vertical
                            pygame.draw.line(screen, BLUE , [map_left, map_up], [map_left,map_down], 2)
                            pygame.draw.line(screen, BLUE , [map_right, map_up], [map_right,map_down], 2)

                            self.map_left=self.map_left-200
                            self.map_right=self.map_right-200
                            

                            pygame.draw.line(screen, BLUE , [map_left, map_up], [map_right,map_up], 2) #startpos, endpos,width
                            pygame.draw.line(screen, BLUE , [map_left, map_down], [map_right,map_down], 2)
                            #vertical
                            pygame.draw.line(screen, BLUE , [map_left, map_up], [map_left,map_down], 2)
                            pygame.draw.line(screen, BLUE , [map_right, map_up], [map_right,map_down], 2)

                            self.map_count-=1
                            print(self.map_count)

                        elif e.key==pygame.K_RETURN:
                            path="simple"+ str(map_count) 
                            self.maptype=path
                            print(path)
                            self.map=False
                            self.mainmenu=True
                            self.single_player=True


                

            elif self.character:
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
                        t = tt.render(self.name[i],True,GREEN)
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
                        t = tt.render(self.name[i],True,GREEN)
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

                        Sonic=  "graphic/character"+ str(i) +".png"      
                        S = pygame.image.load(Sonic).convert()
                        S.set_colorkey(BLACK)
                        r = S.get_rect()
                        r.topleft = (150+(i-12)*100,440)
                        screen.blit(S,r)

                        tt=pygame.font.Font(None,20)
                        t = tt.render(self.name[i],True,GREEN)
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
                            self.mainmenu=True

            

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
            self.dots_group.draw(screen)
            self.enemies.draw(screen)
            screen.blit(self.player.image,self.player.rect)
            #text=self.font.render("Score: "+(str)(self.score), 1,self.RED)
            #screen.blit(text, (30, 650))
            # Render the text for the score
            text = self.font.render("Flags: " + str(self.score),True,GREEN)
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


    
