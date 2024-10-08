# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((480,880))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, 0) 

bloques_estaticos = []


def dibujar_bloques():
    for bloque in bloques_estaticos:
        pygame.draw.rect(screen, "yellow", (bloque[0], bloque[1], 40, 40))

while running:

    num = 0

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")


    
    
    bloque_actual = pygame.draw.rect(screen, "yellow", (player_pos.x, player_pos.y,40,40))
    
    if player_pos.y <= 840 :

        keys = pygame.key.get_pressed()
        if keys[pygame.K_s] and player_pos.y <= 840:
            player_pos.y += 300 * dt
        if keys[pygame.K_a] and player_pos.x >= 0:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d] and player_pos.x <= 440:
            player_pos.x += 300 * dt

        # "Y" bajando a medida que pasa el tiempo
        player_pos.y += 0.05

        if player_pos.y >= 840:
            num += 1 
            bloques_estaticos.append(bloque_actual)
            player_pos.x, player_pos.y = screen.get_width() / 2, 0

        





    dibujar_bloques()
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()