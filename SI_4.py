
import pygame, sys

pygame.init()
clock=pygame.time.Clock()

screen = pygame.display.set_mode((400,600))

#creating objects of game
player=pygame.Rect(200,500,30,30)
playerSpeed=20
enemy=pygame.Rect(70,50,40,40)
enemyspeed= -2;

#Create a list of enemies named "enemies"

#Use for loop to append enemy rectangles in the enemies list.

bullet=pygame.Rect(200,400,5,10)
bulletspeed=5 
bulletState="ready"
        
while True:    
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x -=playerSpeed
            if event.key ==pygame.K_RIGHT:
                player.x +=playerSpeed
            if event.key == pygame.K_SPACE:
                bulletState="fired"
    
    if bulletState == "ready":
        bullet.x=player.x+12
        bullet.y=player.y
    
    if bulletState =="fired":
       bullet.y=bullet.y-bulletspeed
       if bullet.y<0:
           bulletState="ready"

    #Code to move one enemy. Move this code inside a loop that runs for all enemies in the enemies list.               
    enemy.x= enemy.x + enemyspeed
    
    if enemy.x == 0 or enemy.x==380:
        enemyspeed=enemyspeed * -1
        enemy.y= enemy.y + 20
    
    pygame.draw.rect(screen,(123,200,100),enemy)  
    
    pygame.draw.rect(screen,(225,225,15),bullet)         
    pygame.draw.rect(screen,(23,100,100),player)
    
    
    pygame.display.update()
    clock.tick(30)

