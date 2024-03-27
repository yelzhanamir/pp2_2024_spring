import pygame
pygame.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("task 3")
done = False

x = 250
y = 200
radius = 25

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y - radius > 0: 
        y -= 20
    if pressed[pygame.K_DOWN] and y + radius < screen.get_height(): 
        y += 20
    if pressed[pygame.K_LEFT] and x - radius > 0: 
        x -= 20
    if pressed[pygame.K_RIGHT] and x + radius < screen.get_width(): 
        x += 20

    screen.fill((0, 0, 0))
    color = (250, 5, 0)
    pygame.draw.circle(screen, color, (x, y), radius)

    pygame.display.flip()
    clock.tick(30)