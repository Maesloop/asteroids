from circleshape import *
from constants import *
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        
    def draw(self, surface):
        pygame.draw.circle(surface, WHITE, (self.position.x, self.position.y), self.radius, 2)
    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
    def split(self):
        groups = self.groups()
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        if not groups:
            print("Warning: Asteroid not in any groups!")
            return
        random_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = new_velocity1 * 1.2  # Make it 20% faster
        
    
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = new_velocity2 * 1.2  # Make it 20% faster
        
        for group in groups:
            group.add(new_asteroid1)
            group.add(new_asteroid2)