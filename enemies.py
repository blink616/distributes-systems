import pygame
import random
from environment import *
from bullet import *
from spriteAnimation import Animation
import threading
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
explosion_image = "graphic/explosion0.png"


class Enemy(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0
    maptype = ''
    explosion = False
    direction = ""
    shoot = False

    def __init__(self, x, y, xx, yy, filename, walkname, maptype, gameType, blocks_array):
        self.maptype = maptype
        self.change_x = xx
        self.change_y = yy
        self.gameType = gameType
        self.position =  [x,y,xx,yy]
        self.enemy_picture = filename
        self.walk = walkname
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.blocks_array = blocks_array
        # Load image which will be for the animation
        img = pygame.image.load(walkname).convert()

        # Create the animations objects
        self.move_right_animation = Animation(img, 32, 32)
        self.move_left_animation = Animation(
            pygame.transform.flip(img, True, False), 32, 32)
        self.move_up_animation = Animation(
            pygame.transform.rotate(img, 90), 32, 32)
        self.move_down_animation = Animation(
            pygame.transform.rotate(img, 270), 32, 32)
        exp_img = pygame.image.load(explosion_image).convert()
        self.explosion_animation = Animation(exp_img, 30, 30)

        # initial animation

        if self.change_x > 0:
            self.move_right_animation.update(10)
            self.image = self.move_right_animation.get_current_image()
        elif self.change_x < 0:
            self.move_left_animation.update(10)
            self.image = self.move_left_animation.get_current_image()

        if self.change_y > 0:
            self.move_down_animation.update(10)
            self.image = self.move_down_animation.get_current_image()
        elif self.change_y < 0:
            self.move_up_animation.update(10)
            self.image = self.move_up_animation.get_current_image()

            # Save the player image
        self.player_image = pygame.image.load(filename).convert()
        self.player_image.set_colorkey(BLACK)
            
    def update(self):
        if not self.explosion:
            self.rect.x += self.change_x
            self.rect.y += self.change_y
            if self.rect.right < 0:
                self.rect.left = SCREEN_WIDTH
            elif self.rect.left > SCREEN_WIDTH:
                self.rect.right = 0
            if self.rect.bottom < 0:
                self.rect.top = SCREEN_HEIGHT
            elif self.rect.top > SCREEN_HEIGHT:
                self.rect.bottom = 0

            items = self.get_intersection_position(self.maptype)

            
            if self.rect.topleft in items[0]:
                self.direction = random.choice(("left","up","down","right"))
            elif self.rect.topleft in items[1]:
                self.direction = random.choice(("left","right","down"))
            elif self.rect.topleft in items[2]:
                self.direction = random.choice(("left","up","right"))
            elif self.rect.topleft in items[3]:
                self.direction = random.choice(("down","right","up"))
            elif self.rect.topleft in items[4]:
                self.direction = random.choice(("down","left","up"))
            elif self.rect.topleft in items[5]:
                self.direction = random.choice(("down","right"))
            elif self.rect.topleft in items[6]:
                self.direction = random.choice(("down","left"))
            elif self.rect.topleft in items[7]:
                self.direction = random.choice(("up","right"))
            elif self.rect.topleft in items[8]:
                self.direction = random.choice(("up","left"))

            if self.direction == "left":
                if self.change_x == 0:
                    self.change_x = -2
                    self.change_y = 0
                  
                else:
                    self.change_x = 0
                    self.change_y = 0
            elif self.direction == "right":
                if self.change_x == 0:
                    self.change_x = 2
                    self.change_y = 0
                else:
                    self.change_x = 0
                    self.change_y = 0
            elif self.direction == "up":
                if self.change_y == 0:
                    self.change_x = 0
                    self.change_y = -2
                else:
                    self.change_x = 0
                    self.change_y = 0
            elif self.direction == "down":
                if self.change_y == 0:
                    self.change_x = 0
                    self.change_y = 2
                else:
                    self.change_x = 0
                    self.change_y = 0

            # This will cause the animation to start   
            if self.change_x > 0:
                self.move_right_animation.update(10)
                self.image = self.move_right_animation.get_current_image()
            elif self.change_x < 0:
                self.move_left_animation.update(10)
                self.image = self.move_left_animation.get_current_image()

            if self.change_y > 0:
                self.move_down_animation.update(10)
                self.image = self.move_down_animation.get_current_image()
            elif self.change_y < 0:
                self.move_up_animation.update(10)
                self.image = self.move_up_animation.get_current_image()
        elif self.explosion:
            if self.explosion_animation.index == self.explosion_animation.get_length() -1:
                pygame.time.wait(500)
            self.explosion_animation.update(12)
            
            self.image = self.explosion_animation.get_current_image()
   

    def get_intersection_position(self,maptype): #intersections of all types on map
        items3 = []
        items4 = []
        items5 = []
        items6 = []
        items7 = []
        items8 = []
        items9 = []
        items10 = []
        items11 = []
        for i,row in enumerate(enviroment(maptype)):
            for j,item in enumerate(row):
                if item == 3:
                    items3.append((j*32,i*32))
                elif item == 4:
                    items4.append((j*32,i*32))
                elif item == 5:
                    items5.append((j*32,i*32))
                elif item == 6:
                    items6.append((j*32,i*32))
                elif item == 7:
                    items7.append((j*32,i*32))
                elif item == 8:
                    items8.append((j*32,i*32))
                elif item == 9:
                    items9.append((j*32,i*32))
                elif item == 10:
                    items10.append((j*32,i*32))
                elif item == 11:
                    items11.append((j*32,i*32))

        return [items3,items4,items5,items6,items7,items8,items9,items10,items11];

    def create_bullet(self):
        return Bullet(self.rect.x, self.rect.y, self.direction, self.blocks_array)
        