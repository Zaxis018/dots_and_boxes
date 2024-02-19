import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
FONT = pygame.font.Font(None, 36)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_text(text, x, y):
    text_surface = FONT.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(x, y))  # Center the text
    screen.blit(text_surface, text_rect)

def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 200 <= x <= 400:
                    if 150 <= y <= 200:
                        return 'bot'
                    elif 250 <= y <= 300:
                        return '2-player'

        screen.fill((0, 0, 0))
        draw_text('Choose mode:', WIDTH // 2, HEIGHT // 4)
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(200, 150, 200, 50))  # Bot button
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(200, 250, 200, 50))  # 2-player button
        draw_text('Bot', WIDTH // 2, 175)
        draw_text('2-Player', WIDTH // 2, 275)
        pygame.display.flip()

def main():
    mode = main_menu()
    if mode == 'bot':
        # Start game in bot mode
        pass
    elif mode == '2-player':
        # Start game in 2-player mode
        pass

if __name__ == '__main__':
    main()

