import pygame
import circleshape
import constants
import random

class Asteroid(circleshape.CircleShape):
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()

    containers = (asteroid_group, updateable, drawable)


    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        child_vector1 = self.velocity.rotate(random_angle)
        child_vector2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        child_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        child_asteroid1.velocity = child_vector1 * 1.2
        child_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        child_asteroid2.velocity = child_vector2 * 1.2

        print(self.position)

        return (child_asteroid1, child_asteroid2)



        