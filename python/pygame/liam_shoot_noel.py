import pygame
import random
import math
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))

#title and icon
pygame.display.set_caption("kuayraisus")
icon = pygame.image.load('oasis.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('liam.png')
playerImg = pygame.transform.scale(playerImg,(150,80))
playerX = 280
playerY = 480
playerX_change = 0

#enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 3
for i in range(num_of_enemies):
    #enemyImg = pygame.image.load('noel.png')
    #enemyImg = pygame.transform.scale(enemyImg,(150,80))
    #enemyX = random.randrange(0,670)
    #enemyY = random.randrange(50,150)
    #enemyX_change = 0.3
    #enemyY_change = 40
    enemyImgs = pygame.image.load('noel.png')
    enemyImgs = pygame.transform.scale(enemyImgs,(150,80))
    enemyImg.append(enemyImgs) 
    enemyX.append(random.randrange(0,670))
    enemyY.append(random.randrange(50,150)) 
    enemyX_change.append(1) 
    enemyY_change.append(40)
# bullet
#ready = you cant see bullet on the screen
#fire = the bullet is crrently moving
bulletImg = pygame.image.load('bullets.png')
bulletImg = pygame.transform.scale(bulletImg,(20,30))
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 2
bullet_state = "ready"

#score
score_values = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 550
#game over text
over_font = pygame.font.Font('freesansbold.ttf', 32)
def game_over_text(x,y):
    over_text = font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (x,y))

def show_score(x,y):
    score = font.render("Score :"+ str(score_values), True, (255,255,255))
    screen.blit(score, (textX,textY))

def player(x,y):
    screen.blit(playerImg, (x,y))
def enemy(x,y,i):
    screen.blit(enemyImg[i] ,(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+65,y+10))
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY, 2)))
    if distance<27:
        return True
    else:
        return False

#Game Loop
running = True
while running: 
    screen.fill((150,0,0)) #screen RGB color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # press keystroke
        if event.type == pygame.KEYDOWN:
            print('keystole is pressed')
            if event.key == pygame.K_LEFT: 
                playerX_change= -0.6
                #print("left is pressed")
            if event.key == pygame.K_RIGHT: 
                playerX_change = 0.6
                #print("right is pressed")
            
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
                playerX_change = 0
                #print("keystoke has been released")
    
    
    playerX+=playerX_change
    if playerX <= -65:
        playerX = -65
    elif playerX >= 670:
        playerX = 670 
    
    #enemy movement
    for i in range(num_of_enemies):

        #gameover
        if enemyY[i]>400:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text(200,250)
            break
        enemyX[i]+=enemyX_change[i]
        if enemyX[i] <= -65:
            enemyX_change[i] = 1
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i] >= 700:
            enemyX_change[i] = -1
            enemyY[i]+=enemyY_change[i]

        #collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = 'ready'
            score_values+=1
            print(score_values)
            enemyX[i] = random.randrange(0,670)
            enemyY[i] = random.randrange(50,150)
            
        enemy(enemyX[i],enemyY[i],i)
    #bullet movement
    if bullet_state is 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change 
    if bulletY<=0:
        bulletY = 480
        bullet_state = 'ready'
    
        


    player(playerX,playerY)
    show_score(textX, textY)
    pygame.display.update()
 