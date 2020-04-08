# Imports the pygame and random modules
import pygame 
import random  

# Initialize the pygame modules to get everything started.

pygame.init() 

# The screen that will be created needs a width and a height.

screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height)) 

# This creates the player, enemies and prize and gives it the image found in its folder. 

player = pygame.image.load("player.png")
enemy = pygame.image.load("monster.png")
enemy2 = pygame.image.load("enemy.png")
enemy3 = pygame.image.load("image.png")
prize = pygame.image.load("prize.png")

# Get the width and height of the images in order to do boundary detection. 

image_height = player.get_height()
image_width = player.get_width()
enemy_height = enemy.get_height()
enemy_width = enemy.get_width()
enemy2_width = enemy2.get_width()
enemy2_height = enemy2.get_height()
enemy3_width = enemy3.get_width()
enemy3_height = enemy3.get_height()
prize_width = prize.get_width()
prize_height = prize.get_height()

print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))

# Store the positions of the player,enemy and prize as variables so that you can change them later. 

playerXPosition = 100
playerYPosition = 50

# Make the enemy and prize start off screen and at a random y position.

enemyXPosition =  screen_width
enemyYPosition =  random.randint(0, screen_height - enemy_height)

enemy2XPosition =  screen_width
enemy2YPosition =  random.randint(0, screen_height - enemy2_height)

enemy3XPosition =  screen_width
enemy3YPosition =  random.randint(0, screen_height - enemy3_height)


prizeXPosition = screen_width
prizeYPosition = random.randint(0, screen_height - prize_height)


# This checks if the up, down, left and right key is pressed.
# Right now they are not so make them equal to the boolean value (True or False) of False. 
 

keyUp= False
keyDown = False
keyRight = False
keyLeft = False


while 1: # This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit the program by quitting).

    screen.fill(0) # Clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the postion specfied. I.e. (100, 50).
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    
    
    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # This event checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant. 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
        
        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            
     
    
    if keyUp == True:
        # This makes sure that the user does not move the player above the window.
        if playerYPosition > 0 : 
            playerYPosition -= 1
    if keyDown == True:
        # This makes sure that the user does not move the player below the window.
        if playerYPosition < screen_height - image_height:
            playerYPosition += 1
    if keyRight == True:
        # This makes sure the user does not move the player out of the window horizontally to the right
        if playerXPosition < screen_width - image_width:
            playerXPosition += 1
    if keyLeft == True:
         # This makes sure the user does not move the player out of the window horizontally to the left
        if playerXPosition > 0:
            playerXPosition -= 1
    
    
    # Bounding box for the player that checks for collision:
    
    playerBox = pygame.Rect(player.get_rect())
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the enemy:
    
    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    
    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    # Bounding box for the prize

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition


    
    
    # Test collision of all the boxes:
    
    if playerBox.colliderect(enemyBox):
    
        # Display losing status to the user: 
        
        print("You lose!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemy2Box):
    
        
        print("You lose!")
       
        
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemy3Box):
    
        
        print("You lose!")
       
        
        pygame.quit()
        exit(0)

    if playerBox.colliderect(prizeBox):

        print("You Win!")

        
        pygame.quit()
        exit(0)
    
        
    # If all the enemies is off the screen the user wins the game:
    
    if enemyXPosition < 0 - enemy_width:
    
        # Display wining status to the user: 
        
        print("You win!")
        
        # Quite game and exit window: 
        pygame.quit()
        
        exit(0)

    if enemy2XPosition < 0 - enemy2_width:
    
        
        print("You win!")
        
        pygame.quit()
        
        exit(0)

    if enemy3XPosition < 0 - enemy3_width:
    
        
        print("You win!")
        
        pygame.quit()
        
        exit(0)
    
 
    
    # Make enemy and prize approach the player at the listed speed.
    
    enemyXPosition -= 0.25
    enemy2XPosition -= 0.35
    prizeXPosition -= 0.10
    enemy3XPosition -= 0.15
    
   # Game ends here 
  
