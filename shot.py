import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH

class Shot(CircleShape):
    def __init__(self, x, y, radius, shot_colour):
        super().__init__(x, y, radius)
        self.colour = shot_colour

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, self.position, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt


