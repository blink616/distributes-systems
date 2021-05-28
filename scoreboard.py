import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)

class Scoreboard(object):
    state = 0
    clearmap_score = []
    deathmatch_score = []
    
    def __init__(self,headings,font_color=(0,0,0),select_color=(255,0,0),ttf_font=None,font_size=35):
        self.font_color = font_color
        self.select_color = select_color
        self.headings = headings
        self.font = pygame.font.Font(ttf_font,font_size)
        count = 0
        #initialize previous scores
        with open("scoreboard.txt", "r") as filestream:
            for line in filestream:
                thislist = []
                currentline = line.split(",")
                thislist.append(currentline[0])
                thislist.append(currentline[1])
                thislist.append(currentline[2])
                if count < 5:
                    self.clearmap_score.append(thislist)
                else:
                    self.deathmatch_score.append(thislist)
                count = count+1
        
    def display_frame(self,screen):
        j = 3
        jend1 = 12*32
        jend2 = 15*32
        jend3 = 18*32

        #death match and clear map table
        for i in range(2,15):
            if i not in range(8,9):
                pygame.draw.line(screen, BLUE , [j*32, i*32], [j*32+jend3,i*32], 1) #up
                pygame.draw.line(screen, BLUE , [j*32, i*32+32], [j*32+jend3,i*32+32], 1) #down
                pygame.draw.line(screen, BLUE , [j*32, i*32], [j*32,i*32+32], 1) #left
                #column 1
                pygame.draw.line(screen, BLUE , [j*32+jend1, i*32], [j*32+jend1,i*32+32],1) #right
                #column 2
                pygame.draw.line(screen, BLUE , [j*32+jend2, i*32], [j*32+jend2,i*32+32],1) #right
                #column 3
                pygame.draw.line(screen, BLUE , [j*32+jend3, i*32], [j*32+jend3,i*32+32],1) #right

        #headings
        label = self.font.render(self.headings[0],True,self.font_color)
        screen.blit(label,(10.5*32+6, 0.5*32+6))

        label = self.font.render(self.headings[1],True,RED)
        screen.blit(label,(11.5*32+6, 15.5*32+6))

        label = self.font.render("Clear Map",True,self.select_color)    
        screen.blit(label,(3*32+6, 2*32+6))

        label = self.font.render("Flags",True,self.select_color)    
        screen.blit(label,(3*32+6+jend1, 2*32+6))

        label = self.font.render("Time",True,self.select_color)    
        screen.blit(label,(3*32+6+jend2, 2*32+6))

        label = self.font.render("Death Match",True,self.select_color)    
        screen.blit(label,(3*32+6, 9*32+6))

        label = self.font.render("Kills",True,self.select_color)    
        screen.blit(label,(3*32+6+jend2, 9*32+6))

        label = self.font.render("Deaths",True,self.select_color)    
        screen.blit(label,(3*32+6+jend1, 9*32+6))

        #writing clear map scores
        for i in range(0,5):
            label = self.font.render(self.clearmap_score[i][0],True,WHITE)    
            screen.blit(label,(3*32+6, (3+i)*32+6))

            label = self.font.render(self.clearmap_score[i][1],True,WHITE)    
            screen.blit(label,(3*32+6+jend1, (3+i)*32+6))

            label = self.font.render(self.clearmap_score[i][2],True,WHITE)    
            screen.blit(label,(3*32+6+jend2, (3+i)*32+6))

        #writing death match scores
        for i in range(0,5):
            label = self.font.render(self.deathmatch_score[i][0],True,WHITE)    
            screen.blit(label,(3*32+6, (10+i)*32+6))

            label = self.font.render(self.deathmatch_score[i][1],True,WHITE)    
            screen.blit(label,(3*32+6+jend1, (10+i)*32+6))

            label = self.font.render(self.deathmatch_score[i][2],True,WHITE)    
            screen.blit(label,(3*32+6+jend2, (10+i)*32+6))

    def event_handler(self,event):
        if event.type == pygame.KEYDOWN:
            self.state = 0