# Snake AI – Deep Q-Learning

A Snake game built with Python and Pygame, featuring an AI agent trained using Deep Q-Learning (DQN) with PyTorch.

The goal of this project is to develop an AI that learns how to play Snake through trial and error, gradually improving its performance through reinforcement learning.

## Features

- Classic Snake game built with Pygame.
- AI agent trained using Deep Q-Learning.
- Neural network built with PyTorch.
- Experience replay using a memory buffer.
- Short-term and long-term training.
- Model saving and loading.
- Training statistics showing score, record, and average score.

## Technologies Used

- Python
- Pygame
- PyTorch
- NumPy

## Project Structure

```text
Snake game/
├── visualization/
│   ├── visualize_network.py
│   └── snake_ai_architecture.png
├── checkpoints/
│   └── legacy/
├── agent.py
├── game.py
├── main.py
├── model.py
├── train.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

1. Clone this repository:

   ```bash
   https://github.com/aayushpndy/Snake-AI
   ```

2. Navigate into the project folder:

   ```bash
   cd "Snake game"
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment on Windows:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Project

**Play Snake manually:**

```bash
python main.py
```

**Train the AI:**

```bash
python train.py
```

The AI learns through repeated gameplay. Training statistics are displayed in the terminal.

## Training Progress

This project is actively being developed. The AI has completed thousands of training games, and further improvements to its learning performance are ongoing.

## Future Improvements

- Automatic model checkpoints.
- Improved training performance.
- Better AI decision-making.
- Training progress visualization.
- Model evaluation and testing.

## Author

Aayush Pandey
