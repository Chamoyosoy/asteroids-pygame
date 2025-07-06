import pygame
from constants import(
    SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS,
    ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS
)
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()

    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # player.update(dt)
        updatable.update(dt)

        screen.fill("black")

        # player.draw(screen)
        for i in drawable:
            i.draw(screen)

        pygame.display.flip()

        # fps.tick(60)
        dt = fps.tick(60) / 1000

if __name__ == "__main__":
    main()
