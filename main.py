import pygame
import time
import random
pygame.init()
clock = pygame.time.Clock()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
FPS = 20
display_width = 800
display_height = 600
block_size = 20
AppleThickness = 30
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Slither')

#icon = pygame.image.load('apple.png')
#pygame.display.set_icon(icon)


img = pygame.image.load('snakehead.png')
appleimg = pygame.image.load('apple.png')
direction = "right"

smallfont = pygame.font.SysFont("comicsansms" , 25)
medfont = pygame.font.SysFont("comicsansms" , 50)
largefont = pygame.font.SysFont("comicsansms" , 75)

def score(score):
    text = smallfont.render("Score:"+str(score),True,black)
    gameDisplay.blit(text,[0,0])

def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        #gameDisplay.fill(white)
        message_to_screen("Paused",black,-100,"large")
        message_to_screen("Press C to continue or Q to quit",black,25)
        pygame.display.update()
        clock.tick(15)   

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text,True,color)
    elif size == "medium":
        textSurface = medfont.render(text,True,color)
    elif size == "large":
        textSurface = largefont.render(text,True,color)
    return textSurface , textSurface.get_rect()

def message_to_screen(msg,color,y_displace = 0 , size = "small"):
    #screen_text = font.render(msg,True,color)
    #gameDisplay.blit(screen_text,[display_width/2,display_height/2])
    textSurf , textRect = text_objects(msg,color,size)
    textRect.center = (display_width/2 ,display_height/2+y_displace)
    gameDisplay.blit(textSurf , textRect)

def game_intro():
	intro = True
	while intro:
            for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        intro = False
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
	    gameDisplay.fill(white)
	    message_to_screen("Welcome to Slither",green,-100,"large")
	    message_to_screen("The objective of the game is to eat red apples",red, -60)
	    message_to_screen("The more apples you eat, the longer you get",red,-30)
	    message_to_screen("If you run into yourself, or to the edges, you will die",red,0)
            message_to_screen("Press C to play , press p to pause ,  press Q to quit",black,90)
            pygame.display.update()
            clock.tick(15)
            

def snake(block_size , snakeList):

    
    if direction == "right":
        head = pygame.transform.rotate(img , 270)
    if direction == "left":
        head = pygame.transform.rotate(img , 90)
    if direction == "down":
        head = pygame.transform.rotate(img , 180)
    if direction == "up":
        head = img

    gameDisplay.blit(head , (snakeList[-1][0] , snakeList[-1][1]))
  
    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay , green , [XnY[0],XnY[1],block_size,block_size])

def gameLoop():
	global direction
	lead_x = display_width / 2
	lead_y = display_height / 2
	lead_x_change = 0
	lead_y_change = 0
	gameExit = False
	gameOver = False
        randAppleX = round(random.randrange(0,display_width-AppleThickness)/10.0)*10.0
        randAppleY = round(random.randrange(0,display_height-AppleThickness)/10.0)*10.0
        count = 0
        snakeList = []
        snakeLength = 1
	while not gameExit:

	    while gameOver == True:
                gameDisplay.fill(white)
                message_to_screen("Game Over",red,-50,size="large")
	        message_to_screen("Press C to play again, press Q to quit",black,size="medium")
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameOver = False
                        gameExit = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            gameExit = True
                            gameOver = False
                        if event.key == pygame.K_c:
                            gameLoop()
                

	    for event in pygame.event.get():
		if event.type == pygame.QUIT:
		    gameExit = True
		if event.type == pygame.KEYDOWN:
		    if event.key == pygame.K_LEFT:
                        direction = "left"
		        lead_x_change = -block_size
		        lead_y_change = 0
		    if event.key == pygame.K_RIGHT:
                        direction = "right"
		        lead_x_change = block_size
		        lead_y_change = 0
		    if event.key == pygame.K_UP:
                        direction = "up"
		        lead_y_change = -block_size
		        lead_x_change = 0
		    if event.key == pygame.K_DOWN:
                        direction = "down"
		        lead_y_change = block_size
		        lead_x_change = 0
                    if event.key == pygame.K_p:
                        pause()

	    lead_x += lead_x_change 
	    lead_y += lead_y_change
	    if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
		gameOver = True
	    gameDisplay.fill(white)
            message_to_screen("snake game",red)

	    #pygame.draw.rect(gameDisplay,red,[randAppleX,randAppleY,AppleThickness,AppleThickness])
            gameDisplay.blit(appleimg , (randAppleX,randAppleY))
            
            snakeHead = []
            snakeHead.append(lead_x)
            snakeHead.append(lead_y)
            snakeList.append(snakeHead)

            if len(snakeList) > snakeLength:
                del snakeList[0]
          
            for eachSegment in snakeList[:-1]:
                if eachSegment == snakeHead:
                    gameOver = True
            
	    snake(block_size , snakeList)
            score(snakeLength-1)

            pygame.display.update()
            """if lead_x == randAppleX and lead_y == randAppleY:
                count += 1   
                print"points:",count
                randAppleX = round(random.randrange(0,display_width-block_size)/10.0)*10.0
                randAppleY = round(random.randrange(0,display_height-block_size)/10.0)*10.0
                snakeLength += 1"""
            if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
                if lead_y > randAppleY and lead_y < randAppleY + AppleThickness :
                    count += 1   
                    print"points:",count
                    randAppleX = round(random.randrange(0,display_width-AppleThickness)/10.0)*10.0
                    randAppleY = round(random.randrange(0,display_height-AppleThickness)/10.0)*10.0
                    snakeLength += 1

                elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness :
                    count += 1   
                    print"points:",count
                    randAppleX = round(random.randrange(0,display_width-AppleThickness)/10.0)*10.0
                    randAppleY = round(random.randrange(0,display_height-AppleThickness)/10.0)*10.0
                    snakeLength += 1
        
	    clock.tick(FPS)

	"""message_to_screen("You Lose",red)
	pygame.display.update()
	time.sleep(2)""" 
	pygame.quit()
	quit()
game_intro()
gameLoop()

