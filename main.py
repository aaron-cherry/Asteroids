import pygame
import sys
from asteroid import *
from asteroidfield import *
from constants import *
from player import *
from shot import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    print(f"{pygame.get_init()}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroid_group, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shot_group, updateable, drawable)
    asteroid_field = AsteroidField()
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updateable.update(dt)
        for asteroid in asteroid_group:
            if asteroid.collision_check(player1):
                print("Game Over!")
                sys.exit(0)
            for shot in shot_group:
                if asteroid.collision_check(shot):
                    asteroid.kill()
                    shot.kill()
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
