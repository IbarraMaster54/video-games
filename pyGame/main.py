import pygame

#Initial config
pygame.init()

#Create a player screen
WIDTH = 400
HEIGHT = 400

bgColor = (168, 87, 69 )

screen = pygame.display.set_mode((WIDTH, HEIGHT));  #Ancho, alto

pygame.display.set_caption("MY game")


#Main loop
status = True
while(status):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False
    screen.fill(bgColor)
    pygame.display.flip()
    
pygame.quit()