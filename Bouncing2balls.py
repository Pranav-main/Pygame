import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))      
pygame.display.set_caption("2 Bouncing Ball")

ball1_x , ball1_y = 400,300   # ball position
bs1_x , bs1_y = 5,5           # ball speed
ballRad1 = 20                # ball radius

ball2_x , ball2_y = 200,150
bs2_x , bs2_y = 5,5
ballRad2 = 20

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball1_x += bs1_x     #ball movement along the x axis
    ball1_y += bs1_y     #ball movment along the y axis

    ball2_x += bs2_x
    ball2_y += bs2_y

    if ball1_x - ballRad1 < 0 or ball1_x + ballRad1 > 800:  #ball bouncing off logic along x axis
        bs1_x = -bs1_x
    if ball1_y - ballRad1 < 0 or ball1_y + ballRad1 > 600:  #ball bouncing off logic along y axis
        bs1_y = -bs1_y

    if ball2_x - ballRad2 < 0 or ball2_x + ballRad2 > 800:  
        bs2_x = -bs2_x
    if ball2_y - ballRad2 < 0 or ball2_y + ballRad2 > 600:  
        bs2_y = -bs2_y

    screen.fill((255,255,255))

    pygame.draw.circle(screen , (0,0,255), (int(ball1_x) , int(ball1_y)) , ballRad1)
    pygame.draw.circle(screen , (255,0,0), (int(ball2_x) , int(ball2_y)) , ballRad2)

    pygame.display.update()

pygame.quit()