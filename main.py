# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2


    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable,drawable)

    shots = pygame.sprite.Group()
    Shot.containers = (shots,updatable,drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids,updatable,drawable)

    AsteroidField.containers = (updatable,)
    
    player = Player(x,y)
    asteroidfield = AsteroidField()

    screen = pygame.display.set_mode(((SCREEN_WIDTH,SCREEN_HEIGHT)))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        # update the updatable
        updatable.update(dt)

        # check for colission with player
        for object in asteroids:
            if object.colission(player):
                return 0
        
        # check for colission with shot
        for object in asteroids:
            for shot in shots:
                if object.colission(shot):
                    shot.kill()
                    object.split()

        # draw the drawable
        for object in drawable:
            object.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()