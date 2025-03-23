import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))      
pygame.display.set_caption("Bouncing Ball")

bounce_sound = pygame.mixer.Sound("metal-pipe-230698.wav")

ball1_x , ball1_y = 400,300   # ball position
bs1_x , bs1_y = 5,5           # ball speed
ballRad1 = 20                # ball radius

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball1_x += bs1_x     #ball movement along the x axis
    ball1_y += bs1_y     #ball movment along the y axis

    if ball1_x - ballRad1 < 0 or ball1_x + ballRad1 > 800:  #ball bouncing off logic along x axis
        bs1_x = -bs1_x
        bounce_sound.play()
    if ball1_y - ballRad1 < 0 or ball1_y + ballRad1 > 600:  #ball bouncing off logic along y axis
        bs1_y = -bs1_y
        bounce_sound.play()

    screen.fill((255,255,255))

    pygame.draw.circle(screen , (0,0,255), (int(ball1_x) , int(ball1_y)) , ballRad1)

    pygame.display.update()

pygame.quit()