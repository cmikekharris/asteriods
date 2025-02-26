import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
from constants import ASTEROID_MAX_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        pygame.sprite.Sprite.__init__(self, self.containers)
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)

        asteroid_one_angle = self.velocity.rotate(random_angle)
        asteroid_two_angle = self.velocity.rotate(-random_angle)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_one = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid_one.velocity = asteroid_one_angle * 1.2

        asteroid_two = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid_two.velocity = asteroid_two_angle * 1.2

