# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import random
from constants import *
from player import Player
from star import Star
from asteroidfield import AsteroidField
from asteroid import Asteroid

def main():
    # Initialize the game
    pygame.init()
    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # All the objects that can be updated
    updatable = pygame.sprite.Group()
    # All the objects that can be drawn
    drawable = pygame.sprite.Group()
    # All the asteriods
    asteroids = pygame.sprite.Group()

    # Set the containers for the player
    Player.containers = (updatable, drawable)
    # Set the containers for the stars
    Star.containers = (updatable, drawable)
    # Set the containers for the asteriods
    Asteroid.containers = (asteroids, updatable, drawable)
    # Set the containers for the asteroid field
    AsteroidField.containers = (updatable)

    # Create a field of stars
    for _ in range(50):  # 50 stars
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        Star(x, y)

    print("Number of stars:", len([s for s in drawable if isinstance(s, Star)]))
    print("Total drawable objects:", len(drawable))

    # Create the player's ship
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Create the asteroid field
    asteroid_field = AsteroidField()

    dt = 0

    # print(f"Number of drawable objects: {len(drawable)}")

    # Main game loop
    while True:
        # Get all the events that have occurred
        for event in pygame.event.get():
            # If the event is a quit event, exit the game
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        # Fill the screen with black
        # pygame.Surface.fill(screen, (0, 0, 0)) - long version
        screen.fill("black")

        for obj in drawable:
            # print(f"Drawing sprite: {type(obj)}")
            obj.draw(screen)

        # Update the display
        pygame.display.flip()

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                return

        dt = clock.tick(60) / 1000

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()

