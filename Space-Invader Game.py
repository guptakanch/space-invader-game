import pygame
import random
import math
pygame.init()
screen_width=800
screen_height=600

gameWindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Space Invader Game")
icon=pygame.image.load('photos/spaceship.png')
pygame.display.set_icon(icon)

#background
backgroundImg=pygame.image.load('photos/3d-skull-partially-buried-sand-against-night-sky.jpg')
#player
playerImg=pygame.image.load('photos/spaceship (1).png')
playerX=370
playerY=480

def player(x,y):
    gameWindow.blit(playerImg,(x,y))


#enemy
'''enemyImg=pygame.image.load('photos/skull.png')
enemyX=370
enemyY=50

enemyX=random.randint(0,736)
enemyY=random.randint(50,150)
enemyX_change=4
enemyY_change=40
'''
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
no_of_enemy=6

for i in range(no_of_enemy):
    enemyImg.append(pygame.image.load('photos/skull.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(40)
def enemy(x,y,i):
    gameWindow.blit(enemyImg[i],(x,y))


#bullet creation
bulletImg=pygame.image.load('photos/bullet.png')
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=10
bullet_state="ready"

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    gameWindow.blit(bulletImg,(x+16,y+12))

def testcollison(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt(math.pow(enemyX-bulletX,2)+math.pow(enemyY-bulletY,2))
    if distance<27:
        return True
    else:
        return False

score=0
fonnt=pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10

def show_score(x,y):
    score1=fonnt.render("Score :"+str(score),True,(255,255,255))
    gameWindow.blit(score1,(x,y))

text=pygame.font.Font('freesansbold.ttf',72)
def game_over():
    text=fonnt.render("Game Over",True,(255,255,255))
    gameWindow.blit(text,(200,250))

block_update=0.3
playerX_change=0
closewindow=False
white=(255,255,255)
while not closewindow:
    gameWindow.fill(white)
    gameWindow.blit(backgroundImg,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            closewindow=True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-block_update
            if event.key==pygame.K_RIGHT:
                playerX_change=block_update
            if event.key==pygame.K_SPACE:
                if bullet_state=="ready":
                    bulletX=playerX
                    fire_bullet(bulletX,bulletY)

        if event.type == pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change = 0
    playerX+=playerX_change

    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736           #800-64=736


    #enemy movement
    for i in range(no_of_enemy):

        #when the game will be over
        if enemyY[i]>440:
            for j in range(no_of_enemy):
                enemyY[j]=20000
            game_over()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.4
            enemyY[i] += enemyY_change[i]
        collison = testcollison(enemyX[i], enemyY[i], bulletX, bulletY)
        if collison:
            bulletY = 480
            bullet_state = "ready"
            score = score+1
            enemyX[i]=random.randint(0,736)
            enemyY[i]=random.randint(50,150)
        enemy(enemyX[i],enemyY[i], i)
#bullet movement
    if bulletY<=0:
        bulletY=480
        bullet_state="ready"

    if bullet_state=="fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change

        #print(score)
    player(playerX,playerY)

    show_score(textX,textY)
    pygame.display.update()