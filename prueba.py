import pygame

# Inicializa Pygame
pygame.init()

# Colores
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)

# Configurar la ventana
ancho_ventana = 400
alto_ventana = 400
ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))

# Título de la ventana
pygame.display.set_caption("Formas Paralizadas")

# Posición inicial del primer cuadrado
x_cuadrado = 50
y_cuadrado = 50

# Velocidad de movimiento
velocidad = 5

# Estado para saber si el primer cuadrado está paralizado
cuadrado_paralizado = False

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Color de fondo
    ventana.fill(NEGRO)

    if not cuadrado_paralizado:
        # Mueve el cuadrado hacia abajo
        y_cuadrado += velocidad
        
        # Condición para detener el cuadrado
        if y_cuadrado >= 300:
            cuadrado_paralizado = True  # Paraliza el cuadrado cuando llega a esta posición
    
    # Dibuja el primer cuadrado
    pygame.draw.rect(ventana, AZUL, (x_cuadrado, y_cuadrado, 50, 50))

    if cuadrado_paralizado:
        # Dibuja un segundo cuadrado cuando el primero está paralizado
        pygame.draw.rect(ventana, VERDE, (200, 200, 50, 50))

    # Actualiza la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
