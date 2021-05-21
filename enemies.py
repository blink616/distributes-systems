import pygame
import random
from environment import *
from spriteAnimation import Animation

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)

class Enemy(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0
    maptype = ''
    def __init__(self,x,y,xx,yy, filename, walkname, maptype):
        self.maptype= maptype
        self.change_x = xx
        self.change_y = yy
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        # Load image which will be for the animation
        img = pygame.image.load(walkname).convert()
        # Create the animations objects
        self.move_right_animation = Animation(img,32,32)
        self.move_left_animation = Animation(pygame.transform.flip(img,True,False),32,32)
        self.move_up_animation = Animation(pygame.transform.rotate(img,90),32,32)
        self.move_down_animation = Animation(pygame.transform.rotate(img,270),32,32)
        
        #initial animation
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


        # Load explosion image
        img = pygame.image.load("graphic/explosion.png").convert()
        self.explosion_animation = Animation(img,30,30)
        # Save the player image
        self.player_image = pygame.image.load(filename).convert()
        self.player_image.set_colorkey(BLACK)
 

    def update(self,horizontal_blocks,vertical_blocks):
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

        if self.rect.topleft in self.get_intersection_position(self.maptype):
            direction = random.choice(("left","right","up","down"))
            
            if direction == "left" and self.change_x == 0:
                self.change_x = -2
                self.change_y = 0

            elif direction == "right" and self.change_x == 0:
                self.change_x = 2
                self.change_y = 0
            elif direction == "up" and self.change_y == 0:
                self.change_x = 0
                self.change_y = -2
            elif direction == "down" and self.change_y == 0:
                self.change_x = 0
                self.change_y = 2
            
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
    

    def get_intersection_position(self,maptype):
        items = []
        for i,row in enumerate(enviroment(maptype)):
            for j,item in enumerate(row):
                if item == 3:
                    items.append((j*32,i*32))

        return items

            


