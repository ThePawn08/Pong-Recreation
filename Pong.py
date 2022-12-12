import pygame
pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

white = (255, 255, 255)
x = 400
y = 250
height = width = 15
ball_Xvel = ball_Yvel = 2.5
p1_y = p2_y = 210
p1_height = p2_height = 80
p1_score = p2_score = 0
bot1_active = False
bot2_active = False

print(p1_score, "|", p2_score)

def ball_movement():
    global x, y, ball_Xvel, ball_Yvel, p1_height, p2_height, p1_score, p2_score

    collision_tolerance = 8
    if ball.colliderect(p1):
        if abs(p1.right - ball.left) < collision_tolerance:
            ball_Xvel = 5
            p1_height -= 2
    if ball.colliderect(p2):
        if abs(p2.left - ball.right) < collision_tolerance:
            ball_Xvel = -5
            p2_height -= 2

    if (ball.top == 0): 
        ball_Yvel *= -1
    if (ball.bottom == 500):
        ball_Yvel *= -1

    if (ball.right > 800):
        x = 400
        y = 250
        ball_Xvel *= -0.5
        p1_height = p2_height = 80
        p1_score += 1
        print(p1_score, "|", p2_score)

    if (ball.left < 0):
        x = 400
        y = 250
        ball_Xvel *= -0.5
        p1_height = p2_height = 80
        p2_score += 1
        print(p1_score, "|", p2_score)

    x += ball_Xvel 
    y -= ball_Yvel
    
    pygame.draw.rect(screen, white, ball)

def paddle_movement():
    global p1_y, p2_y, bot1_active, bot2_active

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and p1_y > 0:
        p1_y -= 5
        bot1_active = False
    if keys[pygame.K_s] and p1_y < (500-p1_height):
        p1_y += 5
        bot1_active = False
    if keys[pygame.K_UP] and p2_y > 0:
        p2_y -= 5
        bot2_active = False
    if keys[pygame.K_DOWN] and p2_y < (500-p2_height):
        p2_y += 5
        bot2_active = False

    if keys[pygame.K_a]:
        bot1_active = True
    if keys[pygame.K_RIGHT]:
        bot2_active = True

    if bot1_active is True:
        p1_y = (y+7.5) - (p1_height/2)
        if p1_y > (500-p1_height):
            p1_y = (500-p1_height)
        if p1_y < 0:
            p1_y = 0
    if bot2_active is True:
        p2_y = (y+7.5) - (p2_height/2)
        if p2_y > (500-p2_height):
            p2_y = (500-p2_height)
        if p2_y < 0:
            p2_y = 0

    pygame.draw.rect(screen, white, p1)
    pygame.draw.rect(screen, white, p2)

run = True
while run:

    ball = pygame.Rect(x, y, width, height)
    p1 = pygame.Rect(75, p1_y,15, p1_height)
    p2 = pygame.Rect(725, p2_y,15, p2_height)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    screen.fill((0, 0, 0))
    pygame.draw.line(screen, white, (400, 0), (400, 500), 2)
    paddle_movement()
    ball_movement()
		
    pygame.display.update()
    clock.tick(60)