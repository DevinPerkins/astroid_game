import pygame
import sys
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    asteroids = pygame.sprite.Group()
    shot = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shot, updatable, drawable)

    dt = 0
    
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    print("Starting Asteroids!")
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collisions(player):
                print("Game over!")
                sys.exit()
            for bullet in shot:
                if asteroid.collisions(bullet):
                    bullet.kill()
                    asteroid.split()          
                      
        screen.fill((0,0,0))
        for thing in drawable:
            thing.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        




if __name__ == "__main__":
    main()
