import pygame
from circleshape import *
from constants import *
from Shot import *
PLAYER_SHOOT_COOLDOWN = 0.3
class Player(CircleShape):
    def __init__(self, x:int, y:int, shots_group=None):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots_group = shots_group
        self.add(*self.containers)
        self.timer = 0
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if self.timer > 0:
            self.timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)  
        if keys[pygame.K_s]:
            self.move(-dt)  
        if keys[pygame.K_SPACE]:
            self.shoot()
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    def shoot(self):
        if self.timer <= 0:
            if self.shots_group is not None:
                new_shot = Shot(self.position.x, self.position.y)
                shot_direction = pygame.Vector2(0, 1)  # Starting with downward direction
                shot_direction = shot_direction.rotate(self.rotation)  # Rotate to match player direction
                new_shot.velocity = shot_direction * PLAYER_SHOOT_SPEED  # Set velocity based on direction and speed
                self.shots_group.add(new_shot)  # Add to the shots group
        
            self.timer = PLAYER_SHOOT_COOLDOWN
        
        