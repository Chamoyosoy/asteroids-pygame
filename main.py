import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidsFields import AsteroidField
from shoot import Shoot

def main():
    # init pygame, a screen and a clock
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()

    # delta time variable
    dt = 0
    
    # create groups for sprites
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shoots = pygame.sprite.Group()
    
    # add groups to classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shoot.containers = (shoots, updatable, drawable)

    # create a player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # main game loop
    while True:
        # exit the game when click in X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # update all items on the group
        updatable.update(dt)

        # create the background
        screen.fill("black")

        # draw every object on the group
        for i in drawable:
            i.draw(screen)

        for asteroid in asteroids:
            if asteroid.collide(player):
                sys.exit("game over")
            
            for shoot in shoots:
                if asteroid.collide(shoot):
                    asteroid.kill()
                    shoot.kill()

        # Update the screen
        pygame.display.flip()

        # update dt and limit the frame rate to 60 fps
        dt = fps.tick(60) / 1000


if __name__ == "__main__":
    main()
