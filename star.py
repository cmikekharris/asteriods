import pygame
import random
import math

class Star(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Initialize the sprite AND add it to the groups
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.position = pygame.Vector2(x, y)
        # Add variables for twinkling
        self.brightness = random.randint(100, 255)
        self.twinkle_speed = random.uniform(1, 3)
        self.time = random.random() * 6.28  # Random starting phase (2*pi)

    def update(self, dt):
        # Update the brightness using a sine wave
        self.time += dt * self.twinkle_speed
        self.brightness = 155 + int(100 * math.sin(self.time))

    def draw(self, screen):
        # Use the current brightness
        pygame.draw.circle(screen, (self.brightness, self.brightness, self.brightness),
                         (self.position.x, self.position.y), 2)