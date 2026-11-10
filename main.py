import pygame as pg
import random
import time
pg.init()
font = pg.font.SysFont("Arial", 24)   # choose font and size


screen=(600,600)
pg.display.set_caption("Snake AI")
screen=pg.display.set_mode(screen)
running=True
x=100
y=100
speed=20
dx=speed
dy=0

food_x=200
food_y=200
snake_body=[(x,y)]
growth = 0
score=0
start_tick=pg.time.get_ticks()
move_delay=150
last_move_time=pg.time.get_ticks()


clock = pg.time.Clock()

while running:
    current_time=pg.time.get_ticks()
    for temp in pg.event.get():
        if temp.type==pg.QUIT:
            running=False
        if temp.type == pg.KEYDOWN:
            if temp.key == pg.K_RIGHT:
                new_dx=speed
                new_dy=0
                if new_dx!=-dx:
                    dx, dy = new_dx, new_dy
            elif temp.key == pg.K_LEFT:
                new_dx=-speed
                new_dy=0
                if new_dx!=-dx:
                    dx, dy = new_dx, new_dy
            elif temp.key == pg.K_UP:
                new_dx=0
                new_dy=-speed
                if new_dy!=-dy:
                    dx, dy = new_dx, new_dy
            elif temp.key == pg.K_DOWN:
                new_dx=0
                new_dy=speed
                if new_dy!=-dy:
                    dx, dy = new_dx, new_dy

    screen.fill((0, 0, 0))
    
    green=((0,255,0))
    red=((255,0,0))
    seconds = (pg.time.get_ticks() - start_tick) // 1000
    
    for segment in snake_body:
        pg.draw.rect(screen, green, (segment[0], segment[1], 20, 20))

    pg.draw.rect(screen,red,(food_x,food_y,20,20))
    #score text
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    time_text = font.render(f"Time: {seconds}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(time_text, (10, 40))
    if current_time-last_move_time>=move_delay:
        x+=dx
        y+=dy
        last_move_time=current_time
        snake_body.insert(0, (x, y))   # add new head at front
        # check self-collision
        if (x, y) in snake_body[1:]:
            running = False   # game over
    
    #food detection
        if x == food_x  and  y == food_y:
            growth=1
            score+=1
            food_x=random.randrange(0,600,20)
            food_y=random.randrange(0,600,20)
            while (food_x,food_y) in snake_body:
                food_x=random.randrange(0,600,20)
                food_y=random.randrange(0,600,20)
            
        else:
            if growth>0:
                growth-=1
            else:
                snake_body.pop()

    if x < 0 or x> 580 or y<0 or y>580:
        running=False
    




    clock.tick(30)
    if running==False:
        END_text = font.render(f"GAME OVER", True, (255, 255, 255))
        screen.blit(END_text, (300, 300))
        
    pg.display.flip()
pg.quit()