import pygame
import random

# Inicializa Pygame
pygame.init()

# Configurar la pantalla
ancho_ventana = 300
alto_ventana = 600
screen = pygame.display.set_mode((ancho_ventana, alto_ventana))

# Colores
NEGRO = (0, 0, 0)
AMARILLO = (255, 255, 0)

# FPS del juego
clock = pygame.time.Clock()

# Posiciones de los bloques caídos
bloques_estaticos = []

# Crear un bloque en una posición aleatoria
def crear_bloque():
    x = random.randint(0, ancho_ventana // 40 - 1) * 40
    return [x, 0]

# Dibuja todos los bloques en la pantalla
def dibujar_bloques():
    for bloque in bloques_estaticos:
        pygame.draw.rect(screen, AMARILLO, (bloque[0], bloque[1], 40, 40))

# Bloque activo (actual)
bloque_actual = crear_bloque()

# Velocidad de caída del bloque
velocidad = 5

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Fondo de pantalla
    screen.fill(NEGRO)

    # Detectar colisión con el suelo o con bloques caídos
    if bloque_actual[1] + 40 >= alto_ventana or [bloque_actual[0], bloque_actual[1] + 40] in bloques_estaticos:
        # Añadir el bloque actual a los bloques estáticos
        bloques_estaticos.append(bloque_actual)
        # Crear un nuevo bloque
        bloque_actual = crear_bloque()
    else:
        # Mover el bloque hacia abajo
        bloque_actual[1] += velocidad

    # Dibujar el bloque actual
    pygame.draw.rect(screen, AMARILLO, (bloque_actual[0], bloque_actual[1], 40, 40))

    # Dibujar los bloques que ya han caído
    dibujar_bloques()

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar los FPS
    clock.tick(30)

# Salir de Pygame
pygame.quit()

