import pygame
from constants import FONT, SCORE_FONT_SIZE, SCORE_COORDINATES, FONT_COLOUR, BUTTON_FONT_SIZE, BACKGROUND_COLOUR, SCREEN_HEIGHT, SCREEN_WIDTH
from button import Button
from gamestate import GameState

def display_score(screen: pygame.Surface, score: float) -> None:
    font = pygame.font.Font(FONT, SCORE_FONT_SIZE)
    score_surface = font.render(f"Score: {int(score)}", True, (64, 64, 64))
    score_rect = score_surface.get_rect(topleft=SCORE_COORDINATES)
    screen.blit(score_surface, score_rect)


def title_screen(screen: pygame.Surface) -> tuple[GameState, str]:
    start_btn = Button(
        center_position=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2),
        font_size=BUTTON_FONT_SIZE,
        bg_rgb=BACKGROUND_COLOUR,
        text_rgb=FONT_COLOUR,
        text="Start",
        action=GameState.GAME,
    )

    username_input = ""
    # placeholder for now
    buttons = [start_btn]

    text_font = pygame.font.Font(FONT, 25)

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continue

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    username_input = username_input[:-1]
                else:
                    username_input += event.unicode

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BACKGROUND_COLOUR)

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action, username_input
            button.draw(screen)


        input_rect = pygame.Rect((SCREEN_WIDTH/2-200, SCREEN_HEIGHT/2-125), (400, 50)) # left top, width height 125 i.e. 100 + 50/2
        pygame.draw.rect(screen, FONT_COLOUR, input_rect, 2)
        input_surface = text_font.render(username_input, True, FONT_COLOUR)

        screen.blit(input_surface, input_surface.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2-100))) 

        pygame.display.flip()
