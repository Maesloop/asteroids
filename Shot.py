from circleshape import *
from constants import *
class Shot(CircleShape):
    def __init__(self, x, y,):
        super().__init__(x,y,SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)
        self.add(*self.containers)
    def update(self, dt):
    # Move the shot based on its velocity and the time elapsed
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 1)