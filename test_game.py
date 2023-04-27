import pygame

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Main Menu")

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# game loop
run = True
while run:
    screen.fill((52, 78, 91))

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()
