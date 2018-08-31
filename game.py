import pygame
pygame.init()
s_width = 500
s_hight = 500
pygame.display.set_caption('Brick Break-Game')
screen = pygame.display.set_mode((s_width,s_hight))
slider_colr = (0,0,255)
slider_x =  s_width/2
slider_y = 490
slider_width = 150
slider_hit = 15
ball_x = 235
ball_y = 472
ball_r = 7
ball_w = 7
x_vel = 5
y_vel = -4
img = pygame.image.load('slider_img.png')
img = img.convert_alpha()
img_w,img_h=img.get_size()
mouse_x= 0
mouse_y = 0
run = True
ball_move = False

while run:
    check1 = False
    check2 = False
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION:
            mouse_x,mouse_y = event.pos
            if mouse_x<slider_x and slider_x > 115:
                slider_x -= 15
                if ball_move ==  False:
                    ball_x -= 15
            if mouse_x > slider_x and slider_x < 415:
                slider_x += 15
                if ball_move ==  False:
                    ball_x += 15
        if key[pygame.K_SPACE] or event.type == pygame.MOUSEBUTTONUP:
            ball_move = True
    if ball_move == True:
        pygame.time.delay(30)
        ball_x +=x_vel
        ball_y +=y_vel
        if ball_x < 10 or ball_x>485:
            x_vel *= -1
        if ball_y <10:
            y_vel *= -1
        if ball_x < slider_x - (img_h/2) and ball_y==472:
            y_vel *=-1
        if ball_x < slider_x + (img_w/2) - img_h/2 and ball_y==472:
            y_vel *=-1

    screen.fill((0,0,0))
    screen.blit(img, (slider_x -img_w/2,slider_y-img_h/2))
    pygame.draw.circle(screen, (255,0,0) , (ball_x,ball_y), ball_w, ball_r)
    pygame.display.update()
pygame.quit()