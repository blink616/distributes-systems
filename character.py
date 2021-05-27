import pygame

# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)

class character():
    def __init__(self):

        self.count=0
        self.up = 180
        self.down = 280
        self.left = 130
        self.right = 220


    

def all(self,screen):


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
            t = tt.render("Pikachu",True,GREEN)
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
            t = tt.render("Sonic",True,GREEN)
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

            Sonic=  "graphic/character2.png"       
            S = pygame.image.load(Sonic).convert()
            S.set_colorkey(BLACK)
            r = S.get_rect()
            r.topleft = (150+(i-12)*100,440)
            screen.blit(S,r)

            tt=pygame.font.Font(None,20)
            t = tt.render("Blue Sonic",True,GREEN)
            screen.blit(t,[150+(i-12)*100,490])

            pc = pygame.transform.chop(pygame.transform.chop(pikachu_exp, (30,0,0,0)), (30,30,pikachu_exp.get_width(),pikachu_exp.get_height()))
            r = pc.get_rect()
            r.topleft = (180+(i-12)*100,440)
            screen.blit(pc,r)



    def yblock(self,screen,count,up,down,right,left):
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

        return path,character
               