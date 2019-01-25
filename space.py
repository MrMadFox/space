import pygame,random,os
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
infoObject = pygame.display.Info()
sizex=infoObject.current_w
sizey=infoObject.current_h
surface=pygame.display.set_mode((sizex,sizey))
surface.fill((255,255,255));
clock=pygame.time.Clock()
score=0
playerimage = pygame.image.load('hero.png')
playerimage=pygame.transform.scale(playerimage, (sizey//10, sizey//10))
def rectangle(colour,pos):
    pygame.draw.rect(surface,colour,pos)
class bullets:
    def __init__(self,id,x,y):
        self.id=id
        self.x=x
        self.y=y
    def display(self):
        rectangle((0,0,0),(self.x-20,self.y,20,10))
def checkcrash(pos):
    for i in range(len(listlevel1)):
        if listlevel1[i].x <= pos[0] <= listlevel1[i].x + listlevel1[i].width and listlevel1[i].y <= pos[1] <= listlevel1[i].y + listlevel1[i].width:
            listlevel1[i].health -= 1
            if listlevel1[i].health <= 0:
                global score
                score+=1
                listlevel1.pop(i)
            return(1)
    if player.x <= pos[0] <= player.x + player.width and player.y <= pos[1] <= player.y + player.width:
        player.health -= 1
        if player.health <= 0:
            print(score)
            print("Out")
            pygame.quit()
            quit()
        return (1)
    return(0)
class level1:
    def __init__(self):
        self.health=10
        self.id=-1
        self.velocity_y=10
        self.width=sizey//20
        self.x=sizex-self.width
        self.y=random.randint(self.width,sizey-self.width)
        self.colour=(255,0,0)
    def display(self):
        surface.blit(playerimage,(self.x,self.y))

def update():
    surface.fill((255,255,255))
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
#player.health=100
listlevel1=[]
for j in range(3):
    listlevel1.append(level1())
listofbullets=[]

while(1):
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            print(score)
            pygame.quit()
            quit()
    mouse_x,mouse_y=pygame.mouse.get_pos()
    mouse_y-=player.width//2
    playervelocity_x,playervelocity_y=0,(mouse_y-player.y)/10
    player.y+=playervelocity_y
    #listofbullets.append(bullets(1, player.x+player.width, player.y))
    listofbullets.append(bullets(1, player.x+player.width, player.y+player.width//2-5))
    #listofbullets.append(bullets(1, player.x+player.width, player.y+player.width-10))
    for i in range(len(listlevel1)):
        if listlevel1[i].y<=0 or listlevel1[i].y>=sizey-listlevel1[i].width:
            listlevel1[i].velocity_y=-listlevel1[i].velocity_y
        listlevel1[i].y+=listlevel1[i].velocity_y
        if random.randint(0,3)==0:#bullets by bots keep it 0-10
            listofbullets.append(bullets(-1,listlevel1[i].x,listlevel1[i].y))
    j=0
    while(len(listofbullets)>j):
        listofbullets[j].x+=listofbullets[j].id*10
        if not 0<=listofbullets[j].x<=sizex:
            listofbullets.pop(j)
            continue
        if checkcrash((listofbullets[j].x,listofbullets[j].y)):
            listofbullets.pop(j)
        j+=1



    update()
    clock.tick(30)


