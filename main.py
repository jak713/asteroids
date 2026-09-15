from gamestate import GameState
import pygame

#from logger import log_state, log_event
from constants import LINE_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH, FONT, PLAYER_TEXT_FONT_SIZE
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from powerup import PowerUp
import powerup
from powerupfield import PowerUpField
from shot import Shot
from displayfunctions import display_score, title_screen, game_over

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.display.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.font.init()
    text_font = pygame.font.Font(FONT, PLAYER_TEXT_FONT_SIZE)
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()
    dt = 0


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2, font=text_font)

    asteroids = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    PowerUp.containers = (powerups, updatable, drawable)

    AsteroidField.containers = (updatable)
    PowerUpField.containers = (updatable)
    AsteroidField()
    PowerUpField()
    gamestate = GameState.TITLE 
    shots = pygame.sprite.Group() 
    Shot.containers = (shots, updatable, drawable)
    
    score = 0
    is_game_over = False
    
    while True:

        #log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        if is_game_over:
            gamestate = game_over(screen, score)
            is_game_over = False
            score = 0
            for a in asteroids:
                a.kill()
            for p in powerups:
                p.kill()
            for s in shots:
                s.kill()
            player.kill()
            player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2, font=text_font)

        if gamestate == GameState.TITLE:
            gamestate, username = title_screen(screen)
            player.set_username(username)
        
        if gamestate == GameState.GAME:
            screen.fill(color='black')
            updatable.update(dt)

            for p in powerups:
                if player.collides_with(p):
                    p.kill()
                    player.set_power_up()

            for a in asteroids:
                if a.collides_with(player):
                    #log_event("player_hit")
                    is_game_over = True
                    break

                for s in shots:
                    if a.collides_with(s):
                        #log_event("asteroid_shot")
                        s.kill()
                        a.split()
                        score += 100


            for object in drawable:
                object.draw(screen)

            display_score(
                screen,
                score,
            )

            pygame.display.flip()
            time = clock.tick(60)
            dt = min(time/1000, 0.1)

    


if __name__ == "__main__":
    main()
