import pygame
pygame.init() #initialize

screen = pygame.display.set_mode((1280,882))  #screen res
pygame.display.set_caption("Testing session")  # caption


x , y , width , height = 340 , 200 , 100 , 80  # Rectangle proeprties
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    screen.fill((0,0,0))

    pygame.draw.rect(screen , (0,50,100) , (x , y , width  ,height))

    pygame.display.update()


pygame.quit()