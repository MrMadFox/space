import pygame,random,os
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
infoObject = pygame.display.Info()
sizex=infoObject.current_w
sizey=infoObject.current_h
surface=pygame.display.set_mode((sizex,sizey))
surface.fill((0,0,0));
clock=pygame.time.Clock()
def rectangle(colour,pos):
    pygame.draw.rect(surface,colour,pos)
class bullets:
    def __init__(self,id,x,y):
        self.id=id
        self.x=x
        self.y=y
    def display(self):
        rectangle((255,255,255),(self.x-20,self.y,20,10))





class level1:
    def __init__(self):
        self.id=-1
        self.velocity_y=10
        self.width=sizey//20
        self.x=sizex-self.width
        self.y=random.randint(self.width,sizey-self.width)
        self.colour=(255,0,0)
    def display(self):
        rectangle(self.colour,(self.x,self.y,self.width,self.width))

def update():
    surface.fill((0,0,0))
    for i in listofbullets:
        i.display()
    for i in listlevel1:
        i.display()
    player.display()
    pygame.display.update()
player=level1()
player.id=1
player.x=0
player.colour=(0, 255, 0)
player.width=sizey//10
listlevel1=[]
listlevel1.append(level1())
listofbullets=[]
while(1):
    for i in pygame.event.get():
        print(i.type)
        if i.type==pygame.QUIT:
            pygame.quit()
            quit()
    mouse_x,mouse_y=pygame.mouse.get_pos()
    mouse_y-=player.width//2
    playervelocity_x,playervelocity_y=0,(mouse_y-player.y)/10
    player.y+=playervelocity_y
    for i in listlevel1:
        if i.y<=0 or i.y>=sizey-i.width:
            i.velocity_y=-i.velocity_y
        i.y+=i.velocity_y
        if random.randint(0,10)==0:
            listofbullets.append(bullets(-1,i.x,i.y))
    for bullet in listofbullets:
        bullet.x+=bullet.id*10
    listofbullets.append(bullets(1, player.x+player.width, player.y))
    listofbullets.append(bullets(1, player.x+player.width, player.y++player.width//2))
    listofbullets.append(bullets(1, player.x+player.width, player.y+player.width))








    update()
    clock.tick(30)


