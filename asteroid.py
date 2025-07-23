from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if(self.radius > ASTEROID_MIN_RADIUS):
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            angle = random.uniform(20, 50)
            new_vel_1 = self.velocity.rotate(angle)
            new_vel_2 = self.velocity.rotate(-angle)

            as1 = Asteroid(self.position.x, self.position.y, new_radius)
            as2 = Asteroid(self.position.x, self.position.y, new_radius)

            as1.velocity = new_vel_1 * 1.2
            as2.velocity = new_vel_2 * 1.2
        
