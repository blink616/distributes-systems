import pygame
from spriteAnimation import Animation


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
bullet_img = "graphic/bullet1.png"


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, direction, blocks_array):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(bullet_img).convert()
        self.image.set_colorkey(BLACK)
        self.blocks_array = blocks_array
        self.direction = direction
        self.tempx = 0
        self.tempy = 0
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.rect = self.image.get_rect(center=(pos_x+20, pos_y+15))

    def update(self):
        if(self.direction == "right"):
            self.image = pygame.transform.flip(self.image, True, False)
            self.tempx += 3
            for block in pygame.sprite.spritecollide(self, self.blocks_array[3], True):
                if(self.tempx > 0):
                    self.rect.centerx = block.rect.centerx
                    self.tempx = 0
                    self.image = pygame.Surface((0, 0))
            
            self.rect.x += 3

        if(self.direction == "left"):
            self.image = pygame.transform.flip(self.image, True, False)

            self.tempx -= 3
            for block in pygame.sprite.spritecollide(self, self.blocks_array[2], True):
                if(self.tempx < 0):
                    self.rect.centerx = block.rect.centerx
                    self.tempx = 0
                    self.image = pygame.Surface((0, 0))
            self.rect.x -= 3

        if(self.direction == "up"):
            self.image = pygame.transform.rotate(self.image, 90)
            self.image = pygame.transform.flip(self.image, True, False)
            self.tempy -= 3
            for block in pygame.sprite.spritecollide(self, self.blocks_array[0], True):
                if(self.tempy < 0):
                    self.rect.centery = block.rect.centery
                    self.tempy = 0
                    self.image = pygame.Surface((0, 0))
            self.rect.y -= 3

        if(self.direction == "down"):
            self.image = pygame.transform.rotate(self.image, 270)
            self.image = pygame.transform.flip(self.image, True, False)
            self.tempy -= 3
            for block in pygame.sprite.spritecollide(self, self.blocks_array[1], True):
                if(self.tempy < 0):
                    self.rect.centery = block.rect.centery
                    self.tempy = 0
                    self.image = pygame.Surface((0, 0))
            self.rect.y += 3
