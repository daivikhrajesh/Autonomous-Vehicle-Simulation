# utils.py
import numpy as np
from config import SCREEN_WIDTH, SCREEN_HEIGHT

def get_state(vehicle):
    # Normalize the state representation of the vehicle
    max_velocity = 10  # Define a maximum velocity for normalization
    state_x = int(vehicle.x / SCREEN_WIDTH * 10)
    state_y = int(vehicle.y / SCREEN_HEIGHT * 10)
    state_velocity = int(vehicle.velocity / max_velocity * 10)

    # Ensure the state values are within the expected range
    state_x = min(max(state_x, 0), 9)
    state_y = min(max(state_y, 0), 9)
    state_velocity = min(max(state_velocity, 0), 9)

    # Combine the normalized values to create a single state index (simple example)
    state_index = state_x + state_y * 10 + state_velocity * 100
    return state_index

def calculate_reward(vehicle):
    # Example function to calculate the reward based on the vehicle's state
    reward = 0
    # Example reward calculation logic based on specific criteria
    # Adjust as per your simulation's objectives and rules
    return reward

# Other utility functions can be added as needed

def example_utility_function():
    # Example of a generic utility function
    pass
