import pygame
import sys
from pygame.locals import *

class GameSettings:
    def __init__(self):
        self.mode = None
        self.grid_size = None

# Initialize Pygame
pygame.init()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (220, 220, 220)
RED = (255, 0, 0)

# Set up some constants
WIDTH, HEIGHT = 600, 600
FONT_SIZE = 30
FPS = 60

background_image = pygame.image.load("image.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Set up the display
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dots and Boxes")

# Initialize clock
clock = pygame.time.Clock()

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def menu():
    settings = GameSettings()
    font = pygame.font.Font("freesansbold.ttf", FONT_SIZE)
    
    mode_text = font.render("Select Mode:", True, BLACK)
    mode_rect = mode_text.get_rect(center=(WIDTH//2, HEIGHT//3 - 40))
    
    mode_buttons = [
        pygame.Rect(WIDTH//3-WIDTH/6, HEIGHT//3, WIDTH/3, 50),
        pygame.Rect(WIDTH//3+WIDTH/6, HEIGHT//3, WIDTH/3, 50)
    ]
    mode_names = ["2 Player", "AI"]
    mode_colors = [WHITE, WHITE]
    
    grid_text = font.render("Enter Grid Size (3-10):", True, BLACK)
    grid_rect = grid_text.get_rect(center=(WIDTH//2, HEIGHT//2+20))
    
    grid_input_rect = pygame.Rect(WIDTH//2 - 100, HEIGHT//2+60, 200, 50)
    grid_input = ""

    while True:
        WIN.blit(background_image, (0, 0))  # Blit background image
        
        draw_text("Dots and Boxes", font, BLACK, WIN, WIDTH//2, HEIGHT//6)
        WIN.blit(mode_text, mode_rect)
        WIN.blit(grid_text, grid_rect)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if grid_input.isdigit() and settings.mode:
                        grid_size = int(grid_input)
                        if 3 <= grid_size <= 10:
                            settings.grid_size = grid_size
                            return settings
                elif event.key == K_BACKSPACE:
                    grid_input = grid_input[:-1]
                else:
                    grid_input += event.unicode

            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, rect in enumerate(mode_buttons):
                    if rect.collidepoint(mouse_pos):
                        settings.mode = mode_names[i]
                        mode_colors[i] = RED
                    else:
                        mode_colors[i] = WHITE

        pygame.draw.rect(WIN, GRAY, grid_input_rect)
        draw_text(grid_input, font, BLACK, WIN, grid_input_rect.centerx, grid_input_rect.centery)
        
        for i, (rect, color) in enumerate(zip(mode_buttons, mode_colors)):
            pygame.draw.rect(WIN, color, rect)
            pygame.draw.rect(WIN, BLACK, rect, 2)
            draw_text(mode_names[i], font, BLACK, WIN, rect.centerx, rect.centery)

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    settings = menu()
    print("Selected Mode:", settings.mode)
    print("Grid Size:", settings.grid_size)

