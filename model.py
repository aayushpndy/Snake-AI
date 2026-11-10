import torch
import torch.nn as nn
import numpy as np
class Linear_QNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.linear1 = nn.Linear(input_size, hidden_size)
        self.linear2 = nn.Linear(hidden_size, output_size)
    def forward(self,x):
        x=self.linear1(x)
        x=torch.relu(x)
        x=self.linear2(x)
        return x
    def save(self, file_name='model.pth'):
        torch.save(self.state_dict(), file_name)
    def load(self, file_name='model.pth'):
        self.load_state_dict(torch.load(file_name, weights_only=True))

class QTrainer:
    def __init__(self, model, lr, gamma):
        self.lr = lr
        self.gamma = gamma
        self.model = model
        self.optimizer = torch.optim.Adam(model.parameters(), lr=self.lr)
        self.criterion = nn.MSELoss()

    def train_step(self, state, action, reward, next_state,done):
        state = torch.tensor(np.array(state), dtype=torch.float)
        action = torch.tensor(action, dtype=torch.long)
        reward = torch.tensor(reward, dtype=torch.float)
        next_state = torch.tensor(np.array(next_state), dtype=torch.float)
        done = torch.tensor(done, dtype=torch.bool)
        if len(state.shape) == 1:
            state = state.unsqueeze(0)
            next_state = next_state.unsqueeze(0)
            action = action.unsqueeze(0)
            reward = reward.unsqueeze(0)
            done = done.unsqueeze(0)
        
        prediction=self.model(state)
        target=prediction.clone()
        action_index=action.argmax(dim=1)
        with torch.no_grad():
            next_prediction = self.model(next_state)
            max_future_q = torch.max(next_prediction,dim=1)[0]
        for idx in range(len(done)):
            if done[idx]:
                target_value = reward[idx]
            else:
            
                target_value = reward[idx] + self.gamma * max_future_q[idx]
            target[idx][action_index[idx]]=target_value
        loss=self.criterion(target,prediction)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

