import torch
import random
import numpy as np
from collections import deque
from game import SnakeGame
from model import Linear_QNet, QTrainer
import os
class Agent:
    def __init__(self):
        self.n_games = 0 #saves no of games played
        self.memory = deque(maxlen=100_000) #capped at 100000 games
        self.epsilon = 0 # it says how often ai explores by choosing random action instead of relying on its experience
        self.gamma = 0.9
        self.model = Linear_QNet(11, 256, 3)
         #neural network to brain
        if os.path.exists('model.pth'):
            self.model.load()
        self.trainer = QTrainer(self.model, lr=0.001, gamma=self.gamma)
        self.batch_size = 1000
    def get_state(self,game):
        state=game.get_state()
        return state
    def get_action(self,state):
        self.epsilon = max(20, 80 - self.n_games)
        random_value = random.randint(0, 200)
        final_move = [0, 0, 0]
        if random_value < self.epsilon:
            move = random.randint(0, 2)
            final_move[move] = 1
        else:
            state0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state0)
            move = torch.argmax(prediction).item()
            final_move[move] = 1

        return final_move
    
    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))
    
    def train_long_memory(self):
        if not self.memory:
            return
        if len(self.memory) > self.batch_size:
            mini_sample = random.sample(self.memory, self.batch_size)
        else:
            mini_sample = list(self.memory)

        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)
    
    def train_short_memory(self, state, action, reward, next_state, done):
        self.trainer.train_step(state, action, reward, next_state, done)