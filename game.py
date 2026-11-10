import pygame as pg
import random
import numpy as np
class SnakeGame:
    def __init__(self):
        self.x=100
        self.y=100
        self.dx=20
        self.dy=0
        self.speed=20
        self.snake_body=[(self.x,self.y)]
        self.score=0
        self.food_x=random.randrange(0,600,20)
        self.food_y=random.randrange(0,600,20)
        self.growth=0
    def spawn_food(self):
        self.food_x=random.randrange(0,600,20)
        self.food_y=random.randrange(0,600,20)
        while (self.food_x,self.food_y) in self.snake_body:
            self.food_x=random.randrange(0,600,20)
            self.food_y=random.randrange(0,600,20)
    def move(self):
        self.x+=self.dx
        self.y+=self.dy
        self.snake_body.insert(0,(self.x,self.y))
        if self.growth>0:
            self.growth-=1
        else:
            self.snake_body.pop()

    def check_food(self):
        if self.x==self.food_x and self.y==self.food_y:
            self.growth+=1
            self.score+=1
            self.spawn_food()

    def check_collision(self):
        if self.x<0 or self.x>580 or self.y<0 or self.y>580:
            return True
        elif (self.x,self.y) in self.snake_body[1:]:
            return True
        else:
            return False
        
    def is_collision(self,position):
        self.x,self.y=position
        if self.x<0 or self.x>580 or self.y<0 or self.y>580:
            return True
        if position in self.snake_body[1:]:
            return True
        return False

        
    def play_step(self,action):
        reward=0
        game_over=False
        self.turn(action)
        self.move()
        if self.check_collision():
            game_over= True
            reward=-10
            return reward, game_over, self.score
        old_score=self.score
        self.check_food()
        if self.score>old_score:
            reward=10

        return reward, game_over, self.score
    def reset(self):
        self.x=100
        self.y=100
        self.dx=20
        self.dy=0
        self.snake_body=[(self.x,self.y)]
        self.score=0
        self.growth=0
        self.spawn_food()

    def get_state(self):
        dir_l=(self.dx==-20)
        dir_r=(self.dx==20)
        dir_u=(self.dy==-20)
        dir_d=(self.dy==20)
        direction=[dir_l, dir_r, dir_u, dir_d]
        food_direction = [
        self.food_x < self.x,  # Food is left . True means small then snake position  
        self.food_x > self.x,  # Food is right
        self.food_y < self.y,  # Food is above
        self.food_y > self.y   # Food is below
        ]           
        
        
        point_l = (self.x - 20, self.y)
        point_r = (self.x + 20, self.y)
        point_u = (self.x, self.y - 20)
        point_d = (self.x, self.y + 20)

        if dir_r:
            danger_straight=self.is_collision(point_r)
            danger_right=self.is_collision(point_d)
            danger_left=self.is_collision(point_u)
        elif dir_l:
            danger_straight = self.is_collision(point_l)
            danger_right = self.is_collision(point_u)
            danger_left = self.is_collision(point_d)

        elif dir_u:
            danger_straight = self.is_collision(point_u)
            danger_right = self.is_collision(point_r)
            danger_left = self.is_collision(point_l)

        elif dir_d:
            danger_straight = self.is_collision(point_d)
            danger_right = self.is_collision(point_l)
            danger_left = self.is_collision(point_r)

        state = [
                    danger_straight,
                    danger_right,
                    danger_left
                    ] + direction + food_direction
        
        return np.array(state, dtype=int)

    def turn(self, action):
        if action == [1, 0, 0]:
            # Continue straight
            self.new_dx = self.dx
            self.new_dy = self.dy

        elif action == [0, 1, 0]:
            # Turn right
            self.new_dx = -self.dy
            self.new_dy = self.dx

        elif action == [0, 0, 1]:
            # Turn left
            self.new_dx = self.dy
            self.new_dy = -self.dx

        self.dx = self.new_dx
        self.dy = self.new_dy







