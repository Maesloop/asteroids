import pygame
from constants import *
from player import Player
from asteroid import *
from asteroidfield import AsteroidField
import sys
from circleshape import *
from Shot import *



def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids,updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots_group, bullets, updatable, drawable)
    asteroid_field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots_group)
    player.shots_group = shots_group
    while True:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
            
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Collision detected!")  # This should appear if collision happens
                print("Game Over!")
                sys.exit()
        for asteroid in asteroids:
            for bullet in bullets:
                if bullet.collides_with(asteroid):  # Or whatever collision detection you're using
                    bullet.kill()
                    asteroid.split()
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
    