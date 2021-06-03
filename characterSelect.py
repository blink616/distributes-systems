import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW =(255,255,0)

class characterSelect(object):
    def __init__(self):
        #character
        self.count=0
        self.up = 180
        self.down = 280
        self.left = 130
        self.right = 220
        self.temp = ["", "not done"]
        self.name=['Kraken','Lynch','Mad Dog','ODoyle','Psycho','Ranger','Ratchet','Reaper','Rigs','Lightning','Fire-Bred','Iron Heart','Steel Foil','Gorgon','Baal','Azrael','Schizo','Manic']
        
    def display_frame(self, screen):
        if self.temp[1] == "done":
            return self.temp

        tt=pygame.font.Font(None,50)
        t = tt.render("Select Character",True,GREEN)
        screen.blit(t,[270,100])

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

        return self.temp

    def event_handler(self,event, screen):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pygame.draw.line(screen, BLUE , [self.left, self.up], [self.right, self.up], 2) #startpos, endpos,width
                pygame.draw.line(screen, BLUE , [self.left, self.down], [self.right, self.down], 2)
                #vertical
                pygame.draw.line(screen, BLUE , [self.left, self.up], [self.left, self.down], 2)
                pygame.draw.line(screen, BLUE , [self.right, self.up], [self.right, self.down], 2)
                self.up=self.up-120
                self.down=self.down-120
                pygame.draw.line(screen, YELLOW , [self.left, self.up], [self.right, self.up], 2) #startpos, endpos,width
                pygame.draw.line(screen, YELLOW , [self.left, self.down], [self.right, self.down], 2)

                pygame.draw.line(screen, YELLOW , [self.left, self.up], [self.left, self.down], 2)
                pygame.draw.line(screen, YELLOW , [self.right, self.up], [self.right, self.down], 2)
                self.count-=6
                

            elif event.key == pygame.K_RIGHT:
                pygame.draw.line(screen, BLUE , [self.left, self.up], [self.right, self.up], 2) #startpos, endpos,width
                pygame.draw.line(screen, BLUE , [self.left, self.down], [self.right, self.down], 2)
                #vertical
                pygame.draw.line(screen, BLUE , [self.left, self.up], [self.left, self.down], 2)
                pygame.draw.line(screen, BLUE , [self.right, self.up], [self.right, self.down], 2)

                self.left=self.left+100
                self.right=self.right+100

                pygame.draw.line(screen, YELLOW , [self.left, self.up], [self.right, self.up], 2) #startpos, endpos,width
                pygame.draw.line(screen, YELLOW , [self.left, self.down], [self.right, self.down], 2)

                pygame.draw.line(screen, YELLOW , [self.left, self.up], [self.left, self.down], 2)
                pygame.draw.line(screen, YELLOW , [self.right, self.up], [self.right, self.down], 2)

                self.count+=1

            elif event.key == pygame.K_DOWN:
                pygame.draw.line(screen, BLUE , [self.left, self.up], [self.right, self.up], 2) #startpos, endpos,width
                pygame.draw.line(screen, BLUE , [self.left, self.down], [self.right, self.down], 2)
                #vertical
                pygame.draw.line(screen, BLUE , [self.left, self.up], [self.left, self.down], 2)
                pygame.draw.line(screen, BLUE , [self.right, self.up], [self.right, self.down], 2)
                self.up=self.up+120
                self.down=self.down+120

                pygame.draw.line(screen, YELLOW , [self.left, self.up], [self.right, self.up], 2) #startpos, endpos,width
                pygame.draw.line(screen, YELLOW , [self.left, self.down], [self.right, self.down], 2)

                pygame.draw.line(screen, YELLOW , [self.left, self.up], [self.left, self.down], 2)
                pygame.draw.line(screen, YELLOW , [self.right, self.up], [self.right, self.down], 2)
                self.count+=6
       

            elif event.key == pygame.K_LEFT:
                pygame.draw.line(screen, BLUE , [self.left, self.up], [self.right, self.up], 2) #startpos, endpos,width
                pygame.draw.line(screen, BLUE , [self.left, self.down], [self.right, self.down], 2)
                #vertical
                pygame.draw.line(screen, BLUE , [self.left, self.up], [self.left, self.down], 2)
                pygame.draw.line(screen, BLUE , [self.right, self.up], [self.right, self.down], 2)
                self.left=self.left-100
                self.right=self.right-100

                pygame.draw.line(screen, YELLOW , [self.left, self.up], [self.right, self.up], 2) #startpos, endpos,width
                pygame.draw.line(screen, YELLOW , [self.left, self.down], [self.right, self.down], 2)

                pygame.draw.line(screen, YELLOW , [self.left, self.up], [self.left, self.down], 2)
                pygame.draw.line(screen, YELLOW , [self.right, self.up], [self.right, self.down], 2)

                self.count-=1

            elif event.key==pygame.K_RETURN:
                self.temp[0] = str(self.count)
                self.temp[1] = "done"
                return

        self.temp[0] = "path"
        self.temp[1] = "not done"
