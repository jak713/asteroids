import pygame

from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_SHOOT_SPEED, PLAYER_TURN_SPEED, PLAYER_SPEED, POWERUP_DURARTION_SECONDS

from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, font, username: str = ""):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0
        self.power_up_timer = 0
        self.power_up = False
        self.font = font
        self.username = username

    def set_username(self,username:str):
        self.username = username

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

        
    def draw(self, screen):
        coords = self.triangle()
        self.name = self.font.render(self.username, False, "white")
        self.name_rect = self.name.get_rect(midbottom=(self.position[0], self.position[1]-20))
        pygame.draw.polygon(screen, "white", coords, LINE_WIDTH)
        screen.blit(self.name, self.name_rect)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.power_up_timer -= dt
        if self.power_up_timer < 0:
            self.power_up = False
        self.shot_cooldown_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt*-1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt*-1)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        shot_colour = "yellow"
        if self.power_up:
            pass
            shot_colour = "blue"
        elif self.shot_cooldown_timer > 0:
            return
        self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        shot = Shot(self.position.x, self.position.y, self.radius, shot_colour)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation)
        shot.velocity *= PLAYER_SHOOT_SPEED

    def set_power_up(self):
        self.power_up_timer = POWERUP_DURARTION_SECONDS
        self.power_up = True
