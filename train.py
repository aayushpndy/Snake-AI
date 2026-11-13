from agent import Agent
from game import SnakeGame
def train():
    agent=Agent()
    game=SnakeGame()
    record=0
    scores=[

    ]
    while True:
        state_old=agent.get_state(game)
        final_move=agent.get_action(state_old)
        reward, done, score=game.play_step(final_move)
        state_new=agent.get_state(game)
        agent.train_short_memory(state_old
                                 , final_move, reward, state_new, done)
        agent.remember(state_old, final_move, reward, state_new, done)
        if done:
            if score > record:
                record = score
                agent.model.save()
            agent.train_long_memory()
            agent.n_games+=1
            if agent.n_games % 100 == 0:
                agent.save_checkpoint()
            scores.append(score)
            mean_score = sum(scores[-100:]) / len(scores[-100:])
            print(f"Game: {agent.n_games}, Score: {score}, Record:{record}, Average: {mean_score:.2f}")
            game.reset()

if __name__=="__main__":

    train()