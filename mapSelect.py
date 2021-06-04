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

class mapSelect(object):
    def __init__(self):
        #map
        self.map_count=0
        self.map_up=140
        self.map_down=300
        self.map_right=380
        self.map_left=210
        self.temp = ["path", "not done"]

    def display_frame(self, screen):
        if self.temp[1] == "done":
            return self.temp

        title=pygame.font.Font(None,50)
        title = title.render("Select Map",True, GREEN)
        screen.blit(title,[300,90])
     
        for i in range(0,4):
            if i<2:

                pygame.draw.line(screen, BLUE , [210+i*200, 140], [380+i*200,140], 2) #startpos, endpos,width
                pygame.draw.line(screen, BLUE , [210+i*200, 300], [380+i*200,300], 2)

                pygame.draw.line(screen, BLUE , [210+i*200, 140], [210+i*200,300], 2)
                pygame.draw.line(screen, BLUE , [380+i*200, 140], [380+i*200,300], 2)

                m=  "graphic/map"+ str(i) +".jpeg"
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

                m=  "graphic/map"+ str(i) +".jpeg"
                ma = pygame.image.load(m).convert()
                ma = pygame.transform.scale(ma, (150, 150)) 
                ma.set_colorkey(BLACK)
                r = ma.get_rect()
                r.topleft = (220+(i-2)*200,345)
                screen.blit(ma,r)

                tt=pygame.font.Font(None,30)
                t = tt.render("Map"+str(i),True,GREEN)
                screen.blit(t,[260+(i-2)*200,510])


        #horizontal
        pygame.draw.line(screen, YELLOW , [self.map_left, self.map_up], [self.map_right,self.map_up], 2) #startpos, endpos,width
        pygame.draw.line(screen, YELLOW , [self.map_left, self.map_down], [self.map_right,self.map_down], 2)
        #vertical
        pygame.draw.line(screen, YELLOW , [self.map_left, self.map_up], [self.map_left,self.map_down], 2)
        pygame.draw.line(screen, YELLOW , [self.map_right, self.map_up], [self.map_right,self.map_down], 2)

        return self.temp
        
    def event_handler(self, event, screen):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:

                pygame.draw.line(screen, BLUE , [self.map_left, self.map_up], [self.map_right, self.map_up], 2) #startpos, endpos,width
                pygame.draw.line(screen, BLUE , [self.map_left, self.map_down], [self.map_right, self.map_down], 2)
                #vertical
                pygame.draw.line(screen, BLUE , [self.map_left, self.map_up], [self.map_left, self.map_down], 2)
                pygame.draw.line(screen, BLUE , [self.map_right, self.map_up], [self.map_right, self.map_down], 2)

                self.map_up=self.map_up-200
                self.map_down=self.map_down-200

                pygame.draw.line(screen, BLUE , [self.map_left, self.map_up], [self.map_right, self.map_up], 2) #startpos, endpos,width
                pygame.draw.line(screen, BLUE , [self.map_left, self.map_down], [self.map_right, self.map_down], 2)
                #vertical
                pygame.draw.line(screen, BLUE , [self.map_left, self.map_up], [self.map_left, self.map_down], 2)
                pygame.draw.line(screen, BLUE , [self.map_right, self.map_up], [self.map_right, self.map_down], 2)
                self.map_count-=2
               

            elif event.key == pygame.K_RIGHT:

                pygame.draw.line(screen, BLUE , [self.map_left, self.map_up], [self.map_right, self.map_up], 2) #startpos, endpos,width
                pygame.draw.line(screen, BLUE , [self.map_left, self.map_down], [self.map_right, self.map_down], 2)
                #vertical
                pygame.draw.line(screen, BLUE , [self.map_left, self.map_up], [self.map_left, self.map_down], 2)
                pygame.draw.line(screen, BLUE , [self.map_right, self.map_up], [self.map_right, self.map_down], 2)

                self.map_left=self.map_left+200
                self.map_right=self.map_right+200

                pygame.draw.line(screen, BLUE , [self.map_left, self.map_up], [self.map_right, self.map_up], 2) #startpos, endpos,width
                pygame.draw.line(screen, BLUE , [self.map_left, self.map_down], [self.map_right, self.map_down], 2)
                #vertical
                pygame.draw.line(screen, BLUE , [self.map_left, self.map_up], [self.map_left, self.map_down], 2)
                pygame.draw.line(screen, BLUE , [self.map_right, self.map_up], [self.map_right, self.map_down], 2)

                self.map_count+=1

            elif event.key == pygame.K_DOWN:

                pygame.draw.line(screen, BLUE , [self.map_left, self.map_up], [self.map_right, self.map_up], 2) #startpos, endpos,width
                pygame.draw.line(screen, BLUE , [self.map_left, self.map_down], [self.map_right, self.map_down], 2)
                #vertical
                pygame.draw.line(screen, BLUE , [self.map_left, self.map_up], [self.map_left, self.map_down], 2)
                pygame.draw.line(screen, BLUE , [self.map_right, self.map_up], [self.map_right, self.map_down], 2)
                
                self.map_up=self.map_up+200
                self.map_down=self.map_down+200

                pygame.draw.line(screen, BLUE , [self.map_left, self.map_up], [self.map_right, self.map_up], 2) #startpos, endpos,width
                pygame.draw.line(screen, BLUE , [self.map_left, self.map_down], [self.map_right, self.map_down], 2)
                #vertical
                pygame.draw.line(screen, BLUE , [self.map_left, self.map_up], [self.map_left, self.map_down], 2)
                pygame.draw.line(screen, BLUE , [self.map_right, self.map_up], [self.map_right, self.map_down], 2)
                self.map_count+=2

            elif event.key == pygame.K_LEFT:

                pygame.draw.line(screen, BLUE , [self.map_left, self.map_up], [self.map_right, self.map_up], 2) #startpos, endpos,width
                pygame.draw.line(screen, BLUE , [self.map_left, self.map_down], [self.map_right, self.map_down], 2)
                #vertical
                pygame.draw.line(screen, BLUE , [self.map_left, self.map_up], [self.map_left, self.map_down], 2)
                pygame.draw.line(screen, BLUE , [self.map_right, self.map_up], [self.map_right, self.map_down], 2)

                self.map_left=self.map_left-200
                self.map_right=self.map_right-200
                

                pygame.draw.line(screen, BLUE , [self.map_left, self.map_up], [self.map_right, self.map_up], 2) #startpos, endpos,width
                pygame.draw.line(screen, BLUE , [self.map_left, self.map_down], [self.map_right, self.map_down], 2)
                #vertical
                pygame.draw.line(screen, BLUE , [self.map_left, self.map_up], [self.map_left, self.map_down], 2)
                pygame.draw.line(screen, BLUE , [self.map_right, self.map_up], [self.map_right, self.map_down], 2)

                self.map_count-=1


            elif event.key==pygame.K_RETURN:
                self.temp[0] = str(self.map_count)
                self.temp[1] = "done"
                return
                    
        self.temp[0] = "path"
        self.temp[1] = "not done"