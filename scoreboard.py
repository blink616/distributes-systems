import pygame
import math

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

    #for death match score is kills and start_time is deaths, end time is always zero
    def newscore(self, playerName, gametype, score, start_time, end_time):
        indexlower = 10
        if gametype == "clearmap":
            #find highscore position
            for score_tuple in range(5):
                if (self.clearmap_score[score_tuple][1] == "-") or (int(self.clearmap_score[score_tuple][1]) < score) or (int(self.clearmap_score[score_tuple][1]) == score and int(self.clearmap_score[score_tuple][2]) > (math.ceil(end_time - start_time))):
                    indexlower = score_tuple
                    break
                
            #new highscore is made
            if indexlower != 10:
                templist = [playerName, str(score), str(math.ceil(end_time - start_time))]
                self.clearmap_score.insert(indexlower,templist)
                self.clearmap_score.pop()

        if gametype == "deathmatch":
            #find highscore position
            for score_tuple in range(5):
                #here score is kill so kills should be maximum, if same then start_time ie. deaths should be minimum
                if (self.deathmatch_score[score_tuple][2] == "-") or (int(self.deathmatch_score[score_tuple][2]) < score) or (int(self.deathmatch_score[score_tuple][2]) == score and int(self.deathmatch_score[score_tuple][1]) > (start_time)):
                    indexlower = score_tuple
                    break
                
            #new highscore is made
            if indexlower != 10:
                templist = [playerName, str(score), str(start_time)]
                self.deathmatch_score.insert(indexlower,templist)
                self.deathmatch_score.pop()

        #there was a new highscore overall
        if indexlower != 10:
            f = open("scoreboard.txt", "w")
            for x in range(5):
                f.write(self.clearmap_score[x][0] + "," + self.clearmap_score[x][1] + "," + self.clearmap_score[x][2] + ",\n")
            for x in range(5):
                f.write(self.deathmatch_score[x][0] + "," + self.deathmatch_score[x][1] + "," +  self.deathmatch_score[x][2] + ",\n")
            
            f.close()
                