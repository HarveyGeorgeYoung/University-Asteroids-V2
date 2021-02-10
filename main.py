import pygame
pygame.init() 
#defining the colurs used
WHITE = (255, 255, 255)
GRAY = (170,170,170) 
BLACK = (0, 0, 0) 

#defining the window dimentions 
width = 600
height = 400
window = pygame.display.set_mode((width, height))

#defining the size and writing style of the text
smallfont = pygame.font.SysFont('Arial',20) 

#defines the text to be superemposed on the buttons
quit = smallfont.render('Quit Game' , 1, WHITE)
start = smallfont.render('Start Game' , 1, WHITE) 

bg = pygame.image.load('Images/start_bg.jpg')
while True: 
    window.blit(bg, (0, 0))
    mouse = pygame.mouse.get_pos() 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
        #checks to see if the mouse has been pressed or not
        if event.type == pygame.MOUSEBUTTONDOWN: 
              
            #if mouse clicked in same position as the quit button then the game is quit 
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
                pygame.quit() 
            
            #if mouse clicked in same position as the start button then the asteroids code is run
            if width/2 <= mouse[0] <= width/2+140 and height/3 <= mouse[1] <= height/3+40:
                import asteroids
                asteroids

            
    # if the mouse is in certain position then the button is shown as one colour howvwer when the mouse hovers over the button the colour of the button changes
    if width/2.5 <= mouse[0] <= width/2.5+140 and height/3 <= mouse[1] <= height/3+40:
        pygame.draw.rect(window,GRAY,[width/2.5,height/3,140,40]) 
    else: 
        pygame.draw.rect(window,BLACK,[width/2.5,height/3,140,40])  
    
    if width/2.5 <= mouse[0] <= width/2.5+140 and height/2 <= mouse[1] <= height/2+40:
        pygame.draw.rect(window,GRAY,[width/2.5,height/2,140,40]) 
    else: 
        pygame.draw.rect(window,BLACK,[width/2.5,height/2,140,40])
      
    # superimposes the text over the buttons
    window.blit(quit , (width/2.5+20,height/2+10))
    window.blit(start , (width/2.5+20,height/3+10)) 
    
    pygame.display.update() 