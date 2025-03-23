import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Gravity and Damping")

bounce_sound = pygame.mixer.Sound("metal-pipe-230698.wav")

ball_x , ball_y = 400 , 300
bs_x , bs_y = 5 , 5 
ballrad = 30
gravity = 1.5
damping = 0.9

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running  = False

    bs_y += gravity
    
    ball_x += bs_x
    ball_y += bs_y

    if ball_x - ballrad < 0 or ball_x + ballrad > 800:
        bs_x = -bs_x * damping
        bounce_sound.play()
        
    if ball_y - ballrad < 0 or ball_y + ballrad > 600:
        bs_y = -bs_y * damping
        ball_y = 600 - ballrad
        bounce_sound.play()

    

    screen.fill((0,0,0))
    pygame.draw.circle(screen , (255,0,0) , (int(ball_x) , int(ball_y)) , ballrad)
    pygame.display.flip()

pygame.quit()
