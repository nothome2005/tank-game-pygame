import pygame 
import random
import os


pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_icon(pygame.image.load('img/icon.bmp'))
pygame.display.set_caption("World of Tanks")
bullet=player_up = pygame.image.load('img/bullet.png').convert_alpha()
player_up = pygame.image.load('img/tank/tank_up.png').convert_alpha()
player_left = pygame.image.load('img/tank/tank_left.png').convert_alpha()
player_right = pygame.image.load('img/tank/tank_right.png').convert_alpha()
player_down = pygame.image.load('img/tank/tank_down.png').convert_alpha()
evil_up = pygame.image.load('img/evil/tank_evil_up.png').convert_alpha()
evil_left = pygame.image.load('img/evil/tank_evil_left.png').convert_alpha()
evil_right = pygame.image.load('img/evil/tank_evil_right.png').convert_alpha()
evil_down = pygame.image.load('img/evil/tank_evil_down.png').convert_alpha()
menu_logo = pygame.image.load('img/menu/logo.png')
pygame.display.set_icon(pygame.image.load('img/icon.bmp'))
direction=1
e_direct=1
#Переменные
Load=True
game=False
menu=False
generation=False
FPS=30
clock = pygame.time.Clock()
all_sprites=pygame.sprite.Group()
GREEN=(0,255,0)
WIDTH=50
HEIGHT=50
x=100
y=100
speed=5
b1=-10
b2=-10
bullet_speed=7
bullet_direction=False
lock=0
w2=0
wall=1#Стуаень создания карты(максимум=4)
w1=0
r1=random.randint(1,2)#Варианты карт
r2=random.randint(1,2)
r3=random.randint(1,2)
r4=random.randint(1,2)
x2=x
y2=y
evilx=0
evily=550
ee_direct=1
eevilx=400
eevily=0
eeb1=-20
eeb2=-20
b_lock=False
click=1
eb1=-20
eb2=-20
bb_lock=False

f1 = pygame.font.Font(None, 25)
fmenu = pygame.font.Font(None, 70)

blue=(0,0,0)
play = fmenu.render("Play", 14, (200, 115, 95))
play2 = fmenu.render("Exit", 14, (200, 115, 95))

v2=True
v=True

vis=True
vis2=True
mousebuttons = pygame.mouse.get_pressed()
rectx=200
recty=300

#Load
while Load:
    clock.tick(35)
    screen.blit(menu_logo, (75,100))

    
    screen.blit(play, (250, 320))
    screen.blit(play2, (250, 420))
    pygame.draw.rect(screen, blue, 
                 (rectx, recty, 200, 75), 8)

    mousex, mousey = pygame.mouse.get_pos()
    mousebuttons = pygame.mouse.get_pressed()

    pygame.display.flip()
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            Load = False

    if mousex>200 and mousex<400 and mousey>300 and mousey<375:
        recty=300
        blue=(64, 128, 255)
        if mousebuttons[0] == 1:
            if click != (0, 0, 0):
                Load=False
                generation=True
    elif mousex>rectx and mousex<(rectx+200) and mousey>400 and mousey<475:
        recty=400
        blue=(64, 128, 255)
        if mousebuttons[0] == 1:
            if click != (0, 0, 0):
                Load=False
    else:
        blue=(0,0,0)

    

#Geneeration
while generation:
    clock.tick(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            generation = False
    if wall==1: 
        if r1==1:
            minimap_1=pygame.image.load('img/map/var_1.png').convert_alpha()
            r1x1=50
            r1y1=50
            r1x2=150
            r1y2=150

            wall=2
            
        if r1==2:
            minimap_1=pygame.image.load('img/map/var_2.png').convert_alpha()
            r1x1=200
            r1y1=200
            wall=2

    if wall==2: 
        if r2==1:
            minimap_2=pygame.image.load('img/map/var_1.png').convert_alpha()
            r2x1=350
            r2y1=50
            r2x2=450
            r2y2=150
            wall=3
        if r2==2:
            minimap_2=pygame.image.load('img/map/var_2.png').convert_alpha()
            r2x1=500
            r2y1=200
            wall=3

    if wall==3: 
        if r3==1:
            minimap_3=pygame.image.load('img/map/var_1.png').convert_alpha()
            r3x1=50
            r3y1=350
            r3x2=150
            r3y2=450
            wall=4
        if r3==2:
            minimap_3=pygame.image.load('img/map/var_2.png').convert_alpha()
            r3x1=200
            r3y1=500
            wall=4 

    if wall==4: 
        if r4==1:
            minimap_4=pygame.image.load('img/map/var_1.png').convert_alpha()
            r4x1=350
            r4y1=350
            r4x2=450
            r4y2=450
            
        if r4==2:
            minimap_4=pygame.image.load('img/map/var_2.png').convert_alpha()
            r4x1=500
            r4y1=500 
        generation=False
        game=True   

    pygame.display.flip()
    
    

#Game
while game==True:
    
    clock.tick(FPS)
    keys=pygame.key.get_pressed()
    text1 = f1.render(str(x)+"  "+str(y), 2, (255, 255, 255))
    screen.blit(text1, (500, 15))
    mousex, mousey = pygame.mouse.get_pos()
    mousebuttons = pygame.mouse.get_pressed()
    text2 = f1.render(str(mousex)+"  "+str(mousey), 2, (100, 255, 255))
    screen.blit(text2, (50, 15))
    #screen.blit(evil_up,(evilx,evily))



    # Обновление
    screen.blit(bullet,(eeb1,eeb2))
    screen.blit(bullet,(eb1,eb2))
    screen.blit(bullet,(b1,b2))
    screen.blit(minimap_1,(0,0))
    screen.blit(minimap_2,(300,0))
    screen.blit(minimap_3,(0,300))
    screen.blit(minimap_4,(300,300))
    

  
    pygame.display.flip()
    screen.fill((0,0,0))
#Conditionals
    if keys[pygame.K_DOWN] and y<550 and direction!=2:
        direction=2
        
    if keys[pygame.K_UP] and y>0 and direction!=1:
        direction=1
        
    if keys[pygame.K_RIGHT] and x<550 and direction!=4:
        direction=4 
         
    if keys[pygame.K_LEFT] and x>0 and direction!=3:
        direction=3
        
    #Zone
    if x>=0 and x<300 and y>=0 and y<300:
        zone=1
    if x>=300 and x<600 and y>=0 and y<300:
        zone=2
    if x>=0 and x<300 and y>=300 and y<600:
        zone=3
    if x>=300 and x<600 and y>=300 and y<600:
        zone=4
#Направление движения танка
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:   #Диспечер переменных
                if direction==1:
                    way='Up'
                if direction==2:
                    way='Down'
                if direction==3:
                    way='Left'
                if direction==4:
                    way='Right'
                v=True 
                v2=True
                evilx=0
                evily=550
                eevilx=400
                eevily=0

                
                print("<--------------------->")
                print("zone:"+str(zone))
                print("player: "+"x="+str(x), "y=" +str(y))
                print("direction: "+str(direction) +" - "+str(way)) 
                print("r1="+str(r1), " r2="+str(r2)," r3="+str(r3), " r4="+str(r4))
    # Bullet direction          
            if event.key == pygame.K_SPACE and bullet_direction==False:
                bullet_direction=True
                if direction==1:
                    b1=x+23
                    b2=y
                if direction==4:
                    b1=x+50
                    b2=y+23
                if direction==2:
                    b1=x+23
                    b2=y+50
                if direction==3:
                    b1=x
                    b2=y+23
    # Player control
    if keys[pygame.K_LEFT] and x>0 and direction==3:
        x-=speed
        #------------------------------------------------------------
        if zone==1:
            if r1==1 or r1==2:
                if x==(r1x1+45) and y>(r1y1-49) and y<(r1y1+49) :
                    x+=speed

            if r1==1 and x==(r1x2+95) and y>(r1y2-49) and y<(r1y2+49):
                x+=speed
            if r1==1 and x==(r1x2+45) and y>(r1y2+49) and y<(r1y2+99):
                x+=speed
        #------------------------------------------------------------
        if zone==2:
            if r2==1 or r2==2:
                if x==(r2x1+45) and y>(r2y1-49) and y<(r2y1+49) :
                    x+=speed

            if r2==1 and x==(r2x2+95) and y>(r2y2-49) and y<(r2y2+49):
                x+=speed
            if r2==1 and x==(r2x2+45) and y>(r2y2+49) and y<(r2y2+99):
                x+=speed
        #------------------------------------------------------------
        if zone==3:
            if r3==1 or r3==2:
                if x==(r3x1+45) and y>(r3y1-49) and y<(r3y1+49) :
                    x+=speed
            if r3==1 and x==(r3x2+95) and y>(r3y2-49) and y<(r3y2+49):
                x+=speed
            if r3==1 and x==(r3x2+45) and y>(r3y2+49) and y<(r3y2+99):
                x+=speed
        #------------------------------------------------------------
        if zone==4:
            if r4==1 or r4==2:
                if x==(r4x1+45) and y>(r4y1-49) and y<(r4y1+49) :
                    x+=speed
            if r4==1 and x==(r4x2+95) and y>(r4y2-49) and y<(r4y2+49):
                x+=speed
            if r4==1 and x==(r4x2+45) and y>(r4y2+49) and y<(r4y2+99):
                x+=speed
        #------------------------------------------------------------



        
    if keys[pygame.K_RIGHT] and x<550 and direction==4 :
        #------------------------------------------------------------
        if zone==1:
            if r1==1 or r1==2:
                if x==(r1x1-50) and y>(r1y1-49) and y<(r1y1+49) :
                    x-=speed
            if r1==1:
                    if x==(r1x2-50) and y>(r1y2-49) and y<(r1y2+99) :
                        x-=speed
        #------------------------------------------------------------                
        if zone==2:
            if r2==1 or r2==2:
                if x==(r2x1-50) and y>(r2y1-49) and y<(r2y1+49) :
                    x-=speed
            if r2==1:
                if x==(r2x2-50) and y>(r2y2-49) and y<(r2y2+99) :
                    x-=speed
        #------------------------------------------------------------
        if zone==3:
            if r3==1 or r3==2:
                if x==(r3x1-50) and y>(r3y1-49) and y<(r3y1+49) :
                    x-=speed
            if r3==1:
                if x==(r3x2-50) and y>(r3y2-49) and y<(r3y2+99) :
                    x-=speed
        #------------------------------------------------------------
        if zone==4:
            if r4==1 or r4==2:
                if x==(r4x1-50) and y>(r4y1-49) and y<(r4y1+49) :
                    x-=speed
            if r4==1:
                if x==(r4x2-50) and y>(r4y2-49) and y<(r4y2+99) :
                    x-=speed
        #------------------------------------------------------------
        x+=speed

    if keys[pygame.K_UP] and y>0 and direction==1 :
        if zone==1:
            if r1==1 or r1==2:
                if x>=(r1x1-49) and x<(r1x1+49) and y==(r1y1+50):
                    y+=speed

            if r1==1 and x>=(r1x2+49) and x<(r1x2+99) and y==(r1y2+50):
                y+=speed

            if r1==1 and x>=(r1x2-49) and x<(r1x2+49) and y==(r1y2+100):
                y+=speed
        #------------------------------------------------------------    
                    
        if zone==2:
            if  x>=(r2x1-49) and x<(r2x1+49) and y==(r2y1+50):
                y+=speed
            if r2==1 and x>=(r2x2+49) and x<(r2x2+99) and y==(r2y2+50):
                y+=speed

            if r2==1 and x>=(r2x2-49) and x<(r2x2+49) and y==(r2y2+100):
                y+=speed
        #------------------------------------------------------------

        if zone==3:
            if x>=(r3x1-49) and x<(r3x1+49) and y==(r3y1+50):
                y+=speed
            if r3==1 and x>=(r3x2+49) and x<(r3x2+99) and y==(r3y2+50):
                y+=speed

            if r3==1 and x>=(r3x2-49) and x<(r3x2+49) and y==(r3y2+100):
                y+=speed
        #------------------------------------------------------------
        if zone==4:
            if x>=(r4x1-49) and x<(r4x1+49) and y==(r4y1+50):
                y+=speed
            if r4==1 and x>=(r4x2+49) and x<(r4x2+99) and y==(r4y2+50):
                y+=speed

            if r4==1 and x>=(r4x2-49) and x<(r4x2+49) and y==(r4y2+100):
                y+=speed
        #------------------------------------------------------------
        y-=speed

    if keys[pygame.K_DOWN] and y<550 and direction==2 :
        if zone==1:
            if r1==1 or r1==2:
                if x>=(r1x1-49) and x<(r1x1+49) and y==(r1y1-50):
                    y-=speed
            if r1==1:
                if x>=(r1x2-49) and x<(r1x2+99) and y==(r1y2-50):
                    y-=speed
        #------------------------------------------------------------
        if zone==2:
            if r2==1 or r2==2:
                if x>=(r2x1-49) and x<(r2x1+49) and y==(r2y1-50):
                    y-=speed
            if r2==1:
                if x>=(r2x2-49) and x<(r2x2+99) and y==(r2y2-50):
                    y-=speed
        #------------------------------------------------------------
        if zone==3:
            if r3==1 or r3==2:
                if x>=(r3x1-49) and x<(r3x1+49) and y==(r3y1-50):
                    y-=speed
            if r3==1:
                if x>=(r3x2-49) and x<(r3x2+99) and y==(r3y2-50):
                    y-=speed
        #------------------------------------------------------------
        if zone==4:
            if r4==1 or r4==2:
                if x>=(r4x1-49) and x<(r4x1+49) and y==(r4y1-50):
                    y-=speed
            if r4==1:
                if x>=(r4x2-49) and x<(r4x2+99) and y==(r4y2-50):
                    y-=speed
        #------------------------------------------------------------
        y+=speed


    #Bullet
    if b2>-10 and b2<620:
        if direction==1 and lock==0 or lock==1:
            b2-=bullet_speed
            lock=1
        if direction==2 and lock==0 or lock==2:
            b2+=bullet_speed
            lock=2
    if b1>-10 and b1<620:
        if direction==3 and lock==0 or lock==3:
            b1-=bullet_speed
            lock=3
        if direction==4 and lock==0 or lock==4:
            b1+=bullet_speed
            lock=4
    if b2<-5 or b2>615 or b1<-5 or b1>615:
        bullet_direction=False
        lock=0
        b1=-10
        b2=-10
# Space tank position
    if direction==1:
        screen.blit(player_up,(x,y))
    if direction==2:
        screen.blit(player_down,(x,y))
    if direction==3:
        screen.blit(player_left,(x,y))
    if direction==4:
        screen.blit(player_right,(x,y))

    if e_direct==1 and v==True:
        screen.blit(evil_up,(evilx,evily))
    if e_direct==2 and v==True:
        screen.blit(evil_down,(evilx,evily))
    if e_direct==3 and v==True:
        screen.blit(evil_left,(evilx,evily))
    if e_direct==4 and v==True:
        screen.blit(evil_right,(evilx,evily))

    if ee_direct==1 and v2==True:
        screen.blit(evil_up,(eevilx,eevily))
    if ee_direct==2 and v2==True:
        screen.blit(evil_down,(eevilx,eevily))
    if ee_direct==3 and v2==True:
        screen.blit(evil_left,(eevilx,eevily))
    if ee_direct==4 and v2==True:
        screen.blit(evil_right,(eevilx,eevily))

    # Enemy conrol

    # Horizontal
    if evilx<x:
        evilx+=2.5
        e_direct=4
    if evilx>x:
        evilx-=2.5
        e_direct=3
    if evilx==x:
        e_direct=1
        if bb_lock==False and v==True:
            eb1=evilx+24
            eb2=evily
            bb_lock=True
    if eb2<0:
        bb_lock=False
    if bb_lock==True:
        eb2-=8

    #Vertical
    if eevily<y:
        eevily+=2.5
        ee_direct=2
    if eevily>y:
        eevily-=2.5
        ee_direct=1
    if eevily==y:
        ee_direct=3
        if b_lock==False and v2==True and vis2==True:
            eeb1=400
            eeb2=eevily+24
            b_lock=True
    if eeb1<0:
        b_lock=False
    if b_lock==True:
        eeb1-=8
    #Enimy bullet
    if eeb1>x and eeb1<x+45 and eeb2>y and eeb2<y+45:
        x2=x
        y2=y
        evilx=0
        evily=550
        ee_direct=1
        eevilx=400
        eevily=0
        eeb1=-20
        eeb2=-20
        b_lock=False

        eb1=-20
        eb2=-20
        bb_lock=False
        direction=1
        e_direct=1
        x=100
        y=100
        v=True
        v2=True
    if eb1>x and eb1<x+45 and eb2>y and eb2<y+45:
        x2=x
        y2=y
        evilx=0
        evily=550
        ee_direct=1
        eevilx=400
        eevily=0
        eeb1=-20
        eeb2=-20
        b_lock=False

        eb1=-20
        eb2=-20
        bb_lock=False
        direction=1
        e_direct=1
        x=100
        y=100
        v=True 
        v2=True
        

    if b1>eevilx and b1<eevilx+50 and b2>eevily and b2<eevily+50:
        v2=False
    if b2>evily and b2<evily+50 and b1>evilx and b1<evilx+50:
        v=False
    if v==False and v2==False:
        game=False



    #Shot conditional
    
    if y>r1y1-25 and y<r1y1+50 :
        vis2=False

    elif y>r3y1-25 and y<r3y1+50 :
        vis2=False

    elif y>r2y1-25 and y<r2y1+50 :
        vis2=False

    elif y>r4y1-25 and y<r4y1+50 :
        vis2=False

        
    else:
        vis2=True 