# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((480,880))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, 0)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    
    if player_pos.y < 880:

        pygame.draw.rect(screen, "yellow", (player_pos[0],player_pos[1],40,40))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_s] and player_pos.y < 840:
            player_pos.y += 300 * dt
        if keys[pygame.K_a] and player_pos.x > 0:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d] and player_pos.x < 440:
            player_pos.x += 300 * dt

        # "Y" bajando a medida que pasa el tiempo
        if player_pos.y < 840:
            player_pos.y += 0.5
  



    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()