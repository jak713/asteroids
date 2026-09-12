import asyncio
import pygame

#from logger import log_state, log_event
from constants import LINE_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

async def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    print("BEFORE DISPLAY INIT", flush=True)
    pygame.display.init()
    print("AFTER DISPLAY INIT", flush=True)

    print("BEFORE SET MODE", flush=True)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("AFTER SET MODE", flush=True)

    #clock = pygame.time.Clock()
    dt = 0


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    field = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    
    score = 0

    while True:
        #log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color='black')
        updatable.update(dt)

        for a in asteroids:
            if a.collides_with(player):
                #log_event("player_hit")
                print("Game over!")
                print(f"Final Score: {score}")
                return
            for s in shots:
                if a.collides_with(s):
                    #log_event("asteroid_shot")
                    s.kill()
                    a.split()
                    score += 100

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()
        #time = clock.tick(60)
        dt = 1/60

        
        await asyncio.sleep(1 / 60)


if __name__ == "__main__":
    asyncio.run(main())
