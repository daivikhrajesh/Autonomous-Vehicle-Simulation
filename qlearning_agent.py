import numpy as np

class QLearningAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.q_table = np.zeros((state_size, action_size))

    def choose_action(self, state, epsilon):
        # Epsilon-greedy policy
        if np.random.rand() < epsilon:
            return np.random.choice(self.action_size)
        else:
            return np.argmax(self.q_table[state, :])

    def update_q_table(self, state, action, reward, next_state, alpha, gamma):
        # Q-table update using Q-learning formula
        if state < 0 or state >= self.state_size:
            raise ValueError(f"Invalid state: {state}. State should be between 0 and {self.state_size-1}")

        if action < 0 or action >= self.action_size:
            raise ValueError(f"Invalid action: {action}. Action should be between 0 and {self.action_size-1}")

        # Q-table update using Q-learning formula
        self.q_table[state, action] += alpha * (reward + gamma * np.max(self.q_table[next_state, :]) - self.q_table[state, action])

# Example usage and debugging
if __name__ == "__main__":
    state_size = 10
    action_size = 5

    agent = QLearningAgent(state_size, action_size)

    state = 0
    action = 3
    reward = 1.0
    next_state = 1
    alpha = 0.1
    gamma = 0.9

    # Example update call
    agent.update_q_table(state, action, reward, next_state, alpha, gamma)
    print(agent.q_table)
