# import pygame

# pygame.init()
# window = pygame.display.set_mode((200, 200))
# clock = pygame.time.Clock()
# font = pygame.font.SysFont(None, 100)
# counter = 5
# text = font.render(str(counter), True, (0, 128, 0))

# timer_event = pygame.USEREVENT+1
# pygame.time.set_timer(timer_event, 1000)

# run = True
# while run:
#     clock.tick(60)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#         elif event.type == timer_event:
#             counter -= 1
#             text = font.render(str(counter), True, (0, 128, 0))
#             if counter == 0:
#                 pygame.time.set_timer(timer_event, 0)                

#     window.fill((255, 255, 255))
#     text_rect = text.get_rect(center = window.get_rect().center)
#     window.blit(text, text_rect)
#     pygame.display.flip()


# OTHER COUNTDOWN METHOD

import pygame
pygame.init()
screen = pygame.display.set_mode((128, 128))
clock = pygame.time.Clock()

counter, text = 10, '10'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT: 
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'boom!'
        if e.type == pygame.QUIT: 
            run = False

    screen.fill((255, 255, 255))
    screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
    pygame.display.flip()
    clock.tick(60)