import sys, pygame
pygame.init()
FRAMERATE = 30
clock = pygame.time.Clock()
pygame.key.set_repeat(20, 20)

size = width, height = 1280,1024
dx = 0
dy = 0
xspeed = 1
bxspeed = 10
bxspeed2 = 10
bxspeed3 = 10
bxspeed4 = 10
bxspeed5 = 10
jumpPower = 13
gravity = 1.5
white = 255, 255, 255
blue = 0,0,255
purple = 255,0,250
fuchsia = 255,20,147
black = 0,0,0
bounceFactor = -0.7
screen = pygame.display.set_mode(size)
ball = pygame.draw.circle(screen, blue, (50,50), 8, 8)
plat1 = pygame.draw.rect(screen,fuchsia, (0,height - 10,width,10))
plat2 = pygame.draw.rect(screen,fuchsia,(0,600,700,10))
plat3 = pygame.draw.rect(screen,fuchsia,(0,200,600,10))
plat4 = pygame.draw.rect(screen,fuchsia,(0,400,300,10))
plat5 = pygame.draw.rect(screen,fuchsia,(0,800,200,10))
plat6 = pygame.draw.rect(screen,fuchsia,(0,100,400,10))
plat7 = pygame.draw.rect(screen,fuchsia,(0,300,500,10))
plat8 = pygame.draw.rect(screen,fuchsia,(0,500,800,10))
plat9 = pygame.draw.rect(screen,fuchsia,(0,700,100,10))
plat10 = pygame.draw.rect(screen,fuchsia,(765,600,550,10))
plat11 = pygame.draw.rect(screen,fuchsia,(665,200,650,10))
plat12= pygame.draw.rect(screen,fuchsia,(365,400,950,10))
plat13 = pygame.draw.rect(screen,fuchsia,(265,800,1050,10))
plat14 = pygame.draw.rect(screen,fuchsia,(465,100,850,10))
plat15 = pygame.draw.rect(screen,fuchsia,(565,300,750,10))
plat16 = pygame.draw.rect(screen,fuchsia,(865,500,450,10))
plat17 = pygame.draw.rect(screen,fuchsia,(165,700,1150,10))

baddie1 = pygame.draw.rect(screen,black,(400,250,200,8))
baddie2 = pygame.draw.rect(screen,black,(100,450,200,8))
baddie3 = pygame.draw.rect(screen,black,(600,350,200,8))
baddie4 = pygame.draw.rect(screen,black,(800,550,200,8))
baddie5 = pygame.draw.rect(screen,black,(1000,150,200,8))
baddies = [baddie1,baddie2,baddie3]
plats = [plat1,plat2,plat3,plat4,plat5,plat6,plat7,plat8,plat9,plat10,plat11,plat12,plat13,plat14,plat15,plat16,plat17]


while True:
    clock.tick(FRAMERATE)
    for baddie in baddies:
        if baddie1.x > 0:
            bxspeed *= -1
        if baddie1.x < width - baddie1.width:
            bxspeed *= -1
        if baddie2.x > 0:
            bxspeed2 *= -1
        if baddie2.x < width - baddie2.width:
            bxspeed2 *= -1
        if baddie3.x > 0:
            bxspeed3 *= -1
        if baddie3.x < width - baddie3.width:
            bxspeed3 *= -1
        if baddie4.x > 0:
            bxspeed4 *= -1
        if baddie4.x < width - baddie4.width:
            bxspeed4 *= -1
        if baddie5.x > 0:
            bxspeed5 *= -1
        if baddie5.x < width - baddie4.width:
            bxspeed5 *= -1
        
        #bxspeed *= -1

    for baddie in baddies:
        baddie1.x += bxspeed
        baddie2.x += bxspeed2
        baddie3.x += bxspeed3
        baddie4.x += bxspeed4
        baddie5.x += bxspeed5
   
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            
     
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and ball.x > 0:
                dx -= xspeed
        if event.key == pygame.K_RIGHT and ball.x < width - ball.width:
                dx += xspeed
        if event.key == pygame.K_UP and dy < 1 and canJump:
                dy -= jumpPower
                canJump = False

    if dy > 2:
        canJump = True
        
    dy += gravity

    ball = ball.move(dx, dy)

    for plat in plats:
        if ball.colliderect(plat) and dy >= 0:
            ball.bottom = plat.top
            dy*=bounceFactor
        
        for baddie in baddies:
            if ball.colliderect(baddie1):
                ball.bottom = baddie1.top
                ball = pygame.draw.circle(screen, blue, (50,50), 8, 8)
            if ball.colliderect(baddie2):
                ball.bottom = baddie2.top
                ball = pygame.draw.circle(screen, blue, (50,50), 8, 8)
            if ball.colliderect(baddie3):
                ball.bottom = baddie3.top
                ball = pygame.draw.circle(screen, blue, (50,50), 8, 8)
            if ball.colliderect(baddie4):
                ball.bottom = baddie4.top
                ball = pygame.draw.circle(screen, blue, (50,50), 8, 8)
            if ball.colliderect(baddie5):
                ball.bottom = baddie5.top
                ball = pygame.draw.circle(screen, blue, (50,50), 8, 8) 

    
    if ball.x < 0:
        ball.x = 1
        dx *= bounceFactor
    if ball.x > width - ball.width:
        ball.x = width - ball.width
        dx *= bounceFactor

    if ball.y < 0:
        ball.y = 1
        dy *= -0.2


    if dy > 9:
        dy = 9

    screen.fill(white)
    plat1 = pygame.draw.rect(screen,fuchsia, (0,height - 10,width,10))
    plat2 = pygame.draw.rect(screen,fuchsia,(0,600,700,10))
    plat3 = pygame.draw.rect(screen,fuchsia,(0,200,600,10))
    plat4 = pygame.draw.rect(screen,fuchsia,(0,400,300,10))
    plat5 = pygame.draw.rect(screen,fuchsia,(0,800,200,10))
    plat6 = pygame.draw.rect(screen,fuchsia,(0,100,400,10))
    plat7 = pygame.draw.rect(screen,fuchsia,(0,300,500,10))
    plat8 = pygame.draw.rect(screen,fuchsia,(0,500,800,10))
    plat9 = pygame.draw.rect(screen,fuchsia,(0,700,100,10))
    plat10 = pygame.draw.rect(screen,fuchsia,(750,600,550,10))
    plat11 = pygame.draw.rect(screen,fuchsia,(650,200,650,10))
    plat12 = pygame.draw.rect(screen,fuchsia,(350,400,950,10))
    plat13 = pygame.draw.rect(screen,fuchsia,(250,800,1050,10))
    plat14 = pygame.draw.rect(screen,fuchsia,(450,100,850,10))
    plat15 = pygame.draw.rect(screen,fuchsia,(550,300,750,10))
    plat16 = pygame.draw.rect(screen,fuchsia,(850,500,450,10))
    plat17 = pygame.draw.rect(screen,fuchsia,(150,700,1150,10))


    baddie1 = pygame.draw.rect(screen,black,(baddie1.x,baddie1.y,200,8))
    baddie2 = pygame.draw.rect(screen,black,(baddie2.x,baddie2.y,200,8))
    baddie3 = pygame.draw.rect(screen,black,(baddie3.x,baddie3.y,200,8))
    baddie4 = pygame.draw.rect(screen,black,(baddie4.x,baddie4.y,200,8))
    baddie5 = pygame.draw.rect(screen,black,(baddie5.x,baddie5.y,200,8))
    ball = pygame.draw.circle(screen, blue, (ball.x,ball.y),8,8)

    #baddie.move(bdx,bdy)
    #(along,down,length,height)
   
   
    

    print(" baddie.x: " + str(baddie.x))

    pygame.display.flip()

