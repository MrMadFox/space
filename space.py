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
health_x=100
health_y=20
playerimage = pygame.image.load('hero.png')
playerimage=pygame.transform.scale(playerimage, (sizey//10, sizey//10))
back = pygame.image.load("background.png")
back = pygame.transform.scale(back, (sizex, sizey))
playerimage.convert_alpha()
playerimage.set_colorkey((255,255,255))
bulletimage=pygame.image.load("bullet1.png")
bulletimage=pygame.transform.scale(bulletimage,(20,10))
bulletimage.convert_alpha()
bulletimage.set_colorkey((17,17,17))
class bullets:
    def __init__(self,id,x,y):
        self.id=id
        self.x=x
        self.y=y
    def display(self):
        surface.blit(bulletimage,(self.x-20,self.y))
        #rectangle((0,0,0),(self.x-20,self.y,20,10))
def checkcrash(pos,id):
    for i in range(len(listlevel1)):
        if listlevel1[i].x <= pos[0] <= listlevel1[i].x + listlevel1[i].width and listlevel1[i].y <= pos[1] <= listlevel1[i].y + listlevel1[i].width and id!=-1:
            listlevel1[i].health -= 1
            if listlevel1[i].health <= 0:
                global score
                score+=1
                listlevel1.pop(i)
            return(1)
    if player.x <= pos[0] <= player.x + player.width and player.y <= pos[1] <= player.y + player.width and id!=1:
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
        self.velocity_x=-1
        self.width=sizey//20
        self.x=sizex-self.width
        self.y=random.randint(self.width,sizey-self.width)
        self.colour=(255,0,0)
    def display(self):
        surface.blit(playerimage,(self.x,self.y))
def healthbar():
    pygame.draw.rect(surface,(0,0,0),(5,5,health_x,health_y),4)
    pygame.draw.rect(surface,(0,0,255),(5,5,player.health*10,health_y))
def update():
    surface.blit(back, (0, 0))#surface.fill((255,255,255))
    healthbar()
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
firebullet=0
while(1):
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            print(score)
            pygame.quit()
            quit()
    mouse_x,mouse_y=pygame.mouse.get_pos()
    mouse_y-=player.width//2
    playervelocity_x,playervelocity_y=(mouse_x-player.x)/10,(mouse_y-player.y)/10
    player.y+=playervelocity_y
    player.x+=playervelocity_x
    #listofbullets.append(bullets(1, player.x+player.width, player.y))
    if firebullet%3==0:
        listofbullets.append(bullets(1, player.x+player.width, player.y+player.width//2-5))
    #listofbullets.append(bullets(1, player.x+player.width, player.y+player.width-10))
    i=0
    while (i<len(listlevel1)):
        listlevel1[i].x += listlevel1[i].velocity_x
        if listlevel1[i].x<0:
            listlevel1.pop(i)
            continue
        if listlevel1[i].y<=0 or listlevel1[i].y>=sizey-listlevel1[i].width:
            listlevel1[i].velocity_y=-listlevel1[i].velocity_y
        listlevel1[i].y+=listlevel1[i].velocity_y
        listlevel1[i].x+=listlevel1[i].velocity_x
        if random.randint(0,3)==0:#bullets by bots keep it 0-10
            listofbullets.append(bullets(-1,listlevel1[i].x,listlevel1[i].y))
        i+=1
    j=0
    while(len(listofbullets)>j):
        listofbullets[j].x+=listofbullets[j].id*10
        if not 0<=listofbullets[j].x<=sizex:
            listofbullets.pop(j)
            continue
        if checkcrash((listofbullets[j].x,listofbullets[j].y),listofbullets[j].id):
            listofbullets.pop(j)
        j+=1
    firebullet+=1
    firebullet%=3
    update()
    clock.tick(30)