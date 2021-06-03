import pygame
from spriteAnimation import Animation
from bullet import *
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)

class Player(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0
    explosion = False
    game_over = False
    def __init__(self,x,y,playerCharacter,playerWalk,playerExplosion):
        # Call the parent class (sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(playerCharacter).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.direction = "right"
        self.boolx = False
        self.booly = False
        self.blocks_array=[]
        # Load image which will be for the animation
        img = pygame.image.load(playerWalk).convert()
        # Create the animations objects
        self.move_right_animation = Animation(img,32,32)
        self.move_left_animation = Animation(pygame.transform.flip(img,True,False),32,32)
        self.move_up_animation = Animation(pygame.transform.rotate(img,90),32,32)
        self.move_down_animation = Animation(pygame.transform.rotate(img,270),32,32)
        # Load explosion image
        img = pygame.image.load(playerExplosion).convert()
        self.explosion_animation = Animation(img,30,30)
        # Save the player image
        self.player_image = pygame.image.load(playerCharacter).convert()
        self.player_image.set_colorkey(BLACK)

    def update(self,up_blocks,down_blocks,left_blocks,right_blocks):
        self.blocks_array = [up_blocks, down_blocks, left_blocks, right_blocks]
        if not self.explosion:
            if self.rect.right < 0:
                self.rect.left = SCREEN_WIDTH
            elif self.rect.left > SCREEN_WIDTH:
                self.rect.right = 0
            if self.rect.bottom < 0:
                self.rect.top = SCREEN_HEIGHT
            elif self.rect.top > SCREEN_HEIGHT:
                self.rect.bottom = 0
            tempx = self.rect.x
            tempy = self.rect.y
            self.rect.x += self.change_x
            self.rect.y += self.change_y
            # if(self.rect.x-tempx >= 3 or self.rect.x-tempx <=-3):
            #     self.boolx = True
            # if(self.rect.y-tempy >= 3 or self.rect.y-tempy <=-3):
            #     self.booly = True

            # This will stop the user for go up or down when it is inside of the box

            for block in pygame.sprite.spritecollide(self,up_blocks,False):
                if self.change_y < 0:
                    self.rect.centery = block.rect.centery
                    self.change_y = 0
            for block in pygame.sprite.spritecollide(self,down_blocks,False):
                
                if self.change_y > 0:
                    self.rect.centery = block.rect.centery
                    self.change_y = 0
            for block in pygame.sprite.spritecollide(self,left_blocks,False):
                
                if self.change_x < 0:
                    self.rect.centerx = block.rect.centerx
                    self.change_x = 0
            for block in pygame.sprite.spritecollide(self,right_blocks,False):
                
                if self.change_x > 0:
                    self.rect.centerx = block.rect.centerx
                    self.change_x = 0

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
        else:
            if self.explosion_animation.index == self.explosion_animation.get_length() -1:
                pygame.time.wait(500)
                self.game_over = True
            self.explosion_animation.update(12)
            self.image = self.explosion_animation.get_current_image()
            
    temp_direction = ""
    def move_right(self):
        self.change_x = 3
        self.direction = "right"
            
    def move_left(self):
        self.change_x = -3
        self.direction = "left"
        

    def move_up(self):
        self.change_y = -3
        self.direction = "up"

    def move_down(self):
        self.change_y = 3
        self.direction = "down"

    def stop_move_right(self):
        if self.change_x != 0:
            self.image = self.player_image
            self.direction = "right"
        self.change_x = 0

    def stop_move_left(self):
        if self.change_x != 0:
            self.image = pygame.transform.flip(self.player_image,True,False)
            self.direction = "left"
        self.change_x = 0

    def stop_move_up(self):
        if self.change_y != 0:
            self.image = pygame.transform.rotate(self.player_image,90)
            self.direction = "up"
        self.change_y = 0

    def stop_move_down(self):
        if self.change_y != 0:
            self.image = pygame.transform.rotate(self.player_image,270)
            self.direction = "down"
        self.change_y = 0
    def create_bullet(self):
    
        return Bullet(self.rect.x, self.rect.y, self.direction, self.blocks_array)