import random
import pygame
from logger import log_event
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rot = random.uniform(20,50)
        vec1 = self.velocity.rotate(rot)
        vec2 = self.velocity.rotate(rot*-1)
        radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x,self.position.y,radius)
        a1.velocity = vec1*1.2
        a2 = Asteroid(self.position.x,self.position.y,radius)
        a2.velocity = vec2 *1.2
