# Autonomous Vehicle Simulation

This project simulates autonomous vehicles navigating through an environment populated with vehicles, pedestrians, and obstacles using Pygame and Q-learning.

## Features

- **Simulation Environment**: Visualizes vehicles, pedestrians, and obstacles using Pygame.
- **QLearningAgent**: Implements a Q-learning agent to control the behavior of the autonomous vehicle.
- **Collision Detection**: Detects collisions between vehicles, pedestrians, and obstacles.
- **Reward System**: Calculates rewards based on collision avoidance.

## Requirements

- Python 3.x
- Pygame
- NumPy

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/autonomous-vehicle-simulation.git
   cd autonomous-vehicle-simulation
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the simulation:
   ```bash
   python main.py
   ```

2. Follow on-screen instructions to interact with the simulation.

## How It Works

- **Initialization**: The simulation initializes the environment, vehicles, pedestrians, and Q-learning agent.
- **Main Loop**: Continuously updates the positions of vehicles and pedestrians based on their velocities and directions.
- **Collision Detection**: Checks for collisions between vehicles, pedestrians, and obstacles.
- **Q-learning**: The agent uses Q-learning to learn optimal actions based on rewards received from the environment.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.


## Acknowledgements

- Inspired by [Pygame](https://www.pygame.org/)
- Q-learning implementation based on [OpenAI's Spinning Up](https://spinningup.openai.com/)

---

### Notes:
- Replace `your-username` in the clone URL with your actual GitHub username or organization name.
