#main.py

import pygame
import random
from config import *
from qlearning_agent import QLearningAgent

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Autonomous Vehicle Simulation")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Initialize Q-learning agent
agent = QLearningAgent(state_size, action_size)
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor

# Vehicle class to represent different types of vehicles
class Vehicle:
    def __init__(self, position, velocity, vehicle_type):
        self.position = position
        self.velocity = velocity
        self.vehicle_type = vehicle_type
        self.active = True  # Flag to track if vehicle is active

    def update_position(self):
        if self.active:
            self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])

# Function to update the screen
def update_screen(agent_position, vehicles, pedestrians, obstacles):
    screen.fill(WHITE)
    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, GREEN, obstacle)
    # Draw agent vehicle
    pygame.draw.circle(screen, BLACK, agent_position, 10)
    # Draw vehicles
    for vehicle in vehicles:
        if vehicle.active:
            if vehicle.vehicle_type == 'car':
                pygame.draw.rect(screen, RED, pygame.Rect(vehicle.position[0], vehicle.position[1], 20, 10))
            elif vehicle.vehicle_type == 'truck':
                pygame.draw.rect(screen, BLUE, pygame.Rect(vehicle.position[0], vehicle.position[1], 30, 15))
            elif vehicle.vehicle_type == 'bicycle':
                pygame.draw.circle(screen, GREEN, vehicle.position, 5)
    # Draw pedestrians
    for pedestrian in pedestrians:
        pygame.draw.line(screen, BLACK, pedestrian[0], pedestrian[1], 3)
    # Update the display
    pygame.display.flip()

# Main simulation loop
def main():
    running = True
    agent_position = (100, 300)  # Example: Initial position of the agent-controlled vehicle

    # Example: Define multiple obstacles (trees)
    obstacles = [
        pygame.Rect(500, 250, 30, 50),
        pygame.Rect(300, 350, 40, 30),
        pygame.Rect(600, 200, 20, 40)
    ]

    # Example: Initialize vehicles with random positions and velocities
    vehicles = [
        Vehicle((600, 300), (random.randint(1, 3), 0), 'car'),     # Car moving to the right
        Vehicle((400, 250), (-random.randint(1, 3), 0), 'truck'),  # Truck moving to the left
        Vehicle((500, 400), (random.randint(1, 3), 0), 'car'),     # Car moving to the right
        Vehicle((200, 350), (-random.randint(1, 3), 0), 'bicycle') # Bicycle moving to the left
    ]

    # Example: Define pedestrians as straight lines
    pedestrians = [
        ((100, 200), (100, 250), 1),  # Vertical line moving down
        ((200, 150), (200, 200), -1), # Vertical line moving up
        ((300, 250), (300, 300), 1),  # Vertical line moving down
        ((400, 100), (400, 150), -1)  # Vertical line moving up
    ]

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Choose action based on epsilon-greedy policy
        epsilon = 0.1  # Example: Exploration-exploitation trade-off
        action = agent.choose_action(0, epsilon)  # Assuming state is simplified to a single value

        # Simulate environment (Example: Move agent vehicle to the right)
        agent_position = (agent_position[0] + 1, agent_position[1])  # Example: Move right

        # Update positions of vehicles
        for vehicle in vehicles:
            vehicle.update_position()

        # Update positions of pedestrians
        for i in range(len(pedestrians)):
            start, end, direction = pedestrians[i]
            if direction == 1:
                # Move pedestrian down
                pedestrians[i] = ((start[0], start[1] + 1), (end[0], end[1] + 1), 1)
            elif direction == -1:
                # Move pedestrian up
                pedestrians[i] = ((start[0], start[1] - 1), (end[0], end[1] - 1), -1)

        # Check for collision with obstacles
        for obstacle in obstacles:
            if agent_position[0] >= obstacle.left and agent_position[0] <= obstacle.right \
               and agent_position[1] >= obstacle.top and agent_position[1] <= obstacle.bottom:
                # If agent vehicle collides with obstacle, stop or take appropriate action
                print("Agent vehicle crashed into obstacle!")
                # Example: Stop agent vehicle or penalize the agent

        # Check for collision between agent vehicle and pedestrians
        for start, end, _ in pedestrians:
            if start[0] <= agent_position[0] <= end[0] and start[1] <= agent_position[1] <= end[1]:
                # If agent vehicle collides with a pedestrian, stop both
                print("Agent vehicle crashed into a pedestrian!")
                # Example: Stop agent vehicle
                agent_position = (0, agent_position[1])  # Reset agent position
                # Stop all vehicles
                for vehicle in vehicles:
                    vehicle.active = False
                # Stop all pedestrians
                for j in range(len(pedestrians)):
                    pedestrians[j] = (pedestrians[j][0], pedestrians[j][1], 0)  # Set direction to 0 to stop
                break

        # Check for collision between vehicles and pedestrians
        for vehicle in vehicles:
            if not vehicle.active:
                continue  # Skip inactive vehicles
            for j in range(len(pedestrians)):
                start, end, direction = pedestrians[j]
                if direction != 0 and start[0] <= vehicle.position[0] <= end[0] and start[1] <= vehicle.position[1] <= end[1]:
                    # If a vehicle collides with a pedestrian, stop both
                    print(f"{vehicle.vehicle_type.capitalize()} crashed into a pedestrian!")
                    # Example: Stop vehicle
                    vehicle.active = False
                    # Stop pedestrian
                    pedestrians[j] = (start, end, 0)  # Set direction to 0 to stop
                    break

        # Update the screen with the new positions
        update_screen(agent_position, vehicles, pedestrians, obstacles)

        # Control the frame rate
        clock.tick(30)  # Adjust as needed to control the simulation speed

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
