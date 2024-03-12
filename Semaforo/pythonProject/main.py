import pygame
import threading
import time
import sys

# Inicializar pygame
pygame.init()

# Definir colores
NEGRO = (0, 0, 0)
GRIS = (36, 36, 36)
BLANCO = (255, 255, 255)
AMARILLO = (255, 255, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

# Definir dimensiones de la ventana
ANCHO = 800
ALTO = 300


# Definir la clase Semáforo
class Semafaro:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color_verde = NEGRO
        self.color_amarillo = NEGRO
        self.color_rojo = ROJO
        self.estado = "ROJO"

    def cambiar_color(self):
        if self.estado == "ROJO":
            self.color_verde = VERDE
            self.color_amarillo = NEGRO
            self.color_rojo = NEGRO
            self.estado = "VERDE"
        elif self.estado == "VERDE":
            # Parpadeo antes de cambiar a amarillo
            parpadeo_count = 0
            while parpadeo_count < 5:
                self.color_verde = NEGRO
                self.color_amarillo = NEGRO
                self.color_rojo = NEGRO
                time.sleep(0.5)  # Tiempo de cada parpadeo
                self.color_verde = VERDE
                self.color_amarillo = NEGRO
                self.color_rojo = NEGRO
                time.sleep(0.5)  # Tiempo de cada parpadeo
                parpadeo_count += 1

            # Cambiar a amarillo después del parpadeo
            self.color_verde = NEGRO
            self.color_amarillo = AMARILLO
            self.estado = "AMARILLO"
        elif self.estado == "AMARILLO":
            self.color_amarillo = NEGRO
            self.color_rojo = ROJO
            self.estado = "ROJO"

    def dibujar_horizontal(self, pantalla):
        # Dibujar los círculos que representan los colores del semáforo
        pygame.draw.circle(pantalla, self.color_verde, (self.x, self.y - 10), 5)
        pygame.draw.circle(pantalla, self.color_amarillo, (self.x, self.y), 5)
        pygame.draw.circle(pantalla, self.color_rojo, (self.x, self.y + 10), 5)

    def dibujar_vertical(self, pantalla):
        # Dibujar los círculos que representan los colores del semáforo
        pygame.draw.circle(pantalla, self.color_verde, (self.x - 10, self.y), 5)
        pygame.draw.circle(pantalla, self.color_amarillo, (self.x, self.y), 5)
        pygame.draw.circle(pantalla, self.color_rojo, (self.x + 10, self.y), 5)

    def dibujar_vertical_inferior(self, pantalla):
        # Dibujar los círculos que representan los colores del semáforo
        pygame.draw.circle(pantalla, self.color_verde, (self.x + 10, self.y), 5)
        pygame.draw.circle(pantalla, self.color_amarillo, (self.x, self.y), 5)
        pygame.draw.circle(pantalla, self.color_rojo, (self.x - 10, self.y), 5)


# Función para cambiar el estado de los semáforos horizontales
def cambiar_semaforo_horizontal(semH):
    while True:
        # Cambiar el color del semáforo horizontal
        semH.cambiar_color()
        # Esperar 11 segundos en verde, 1 segundo en amarillo, 10 segundos en rojo
        time.sleep(11)
        semH.cambiar_color()
        time.sleep(1)
        semH.cambiar_color()
        time.sleep(16)


# Función para cambiar el estado de los semáforos verticales
def cambiar_semaforo_vertical(semV):
    while True:
        # Cambiar el color del semáforo vertical
        semV.cambiar_color()
        # Esperar 9 segundos en verde, 1 segundo en amarillo, 12 segundos en rojo
        time.sleep(10)
        semV.cambiar_color()
        time.sleep(1)
        semV.cambiar_color()
        time.sleep(17)


# Crear semáforos
semaforo_1 = Semafaro(229, 185)
semaforo_2 = Semafaro(457, 185)
semaforo_3 = Semafaro(686, 185)
semaforo_4 = Semafaro(130, 205)
semaforo_5 = Semafaro(440, 95)
semaforo_6 = Semafaro(586, 205)

# Iniciar los threads para cada semáforo
thread_semH1 = threading.Thread(target=cambiar_semaforo_horizontal, args=(semaforo_1,))
thread_semH2 = threading.Thread(target=cambiar_semaforo_horizontal, args=(semaforo_2,))
thread_semH3 = threading.Thread(target=cambiar_semaforo_horizontal, args=(semaforo_3,))
thread_semV4 = threading.Thread(target=cambiar_semaforo_vertical, args=(semaforo_4,))
thread_semV5 = threading.Thread(target=cambiar_semaforo_vertical, args=(semaforo_5,))
thread_semV6 = threading.Thread(target=cambiar_semaforo_vertical, args=(semaforo_6,))

# Iniciar los threads
thread_semH1.start()
time.sleep(1)
thread_semH2.start()
time.sleep(1)
thread_semH3.start()
time.sleep(15)
thread_semV4.start()
time.sleep(1)
thread_semV5.start()
time.sleep(1)
thread_semV6.start()

# Configurar pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Simulador de Semaforos")


# Función para salir del programa
def salir():
    pygame.quit()
    sys.exit()


# Crear botón de salir
boton_salir = pygame.Rect(700, 10, 80, 30)

# Ciclo del juego
terminado = False
reloj = pygame.time.Clock()

while not terminado:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            terminado = True
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  # Botón izquierdo del ratón
                if boton_salir.collidepoint(evento.pos):
                    salir()

    # Limpiar pantalla
    pantalla.fill(GRIS)

    # Dibujar líneas de la avenida
    pygame.draw.line(pantalla, AMARILLO, (0, ALTO // 3), (ANCHO // 7, ALTO // 3), 5)
    pygame.draw.line(pantalla, AMARILLO, (2 * ANCHO // 7, ALTO // 3), (3 * ANCHO // 7, ALTO // 3), 5)
    pygame.draw.line(pantalla, AMARILLO, (4 * ANCHO // 7, ALTO // 3), (5 * ANCHO // 7, ALTO // 3), 5)
    pygame.draw.line(pantalla, AMARILLO, (6 * ANCHO // 7, ALTO // 3), (ANCHO, ALTO // 3), 5)
    pygame.draw.line(pantalla, AMARILLO, (ANCHO // 7, 0), (ANCHO // 7, ALTO // 3), 5)
    pygame.draw.line(pantalla, AMARILLO, (ANCHO // 7, 2 * ALTO // 3), (ANCHO // 7, ALTO), 5)
    pygame.draw.line(pantalla, AMARILLO, (2 * ANCHO // 7, 0), (2 * ANCHO // 7, ALTO // 3), 5)
    pygame.draw.line(pantalla, AMARILLO, (2 * ANCHO // 7, 2 * ALTO // 3), (2 * ANCHO // 7, ALTO), 5)
    pygame.draw.line(pantalla, AMARILLO, (3 * ANCHO // 7, 0), (3 * ANCHO // 7, ALTO // 3), 5)
    pygame.draw.line(pantalla, AMARILLO, (3 * ANCHO // 7, 2 * ALTO // 3), (3 * ANCHO // 7, ALTO), 5)
    pygame.draw.line(pantalla, AMARILLO, (4 * ANCHO // 7, 0), (4 * ANCHO // 7, ALTO // 3), 5)
    pygame.draw.line(pantalla, AMARILLO, (4 * ANCHO // 7, 2 * ALTO // 3), (4 * ANCHO // 7, ALTO), 5)
    pygame.draw.line(pantalla, AMARILLO, (5 * ANCHO // 7, 0), (5 * ANCHO // 7, ALTO // 3), 5)
    pygame.draw.line(pantalla, AMARILLO, (5 * ANCHO // 7, 2 * ALTO // 3), (5 * ANCHO // 7, ALTO), 5)
    pygame.draw.line(pantalla, AMARILLO, (6 * ANCHO // 7, 0), (6 * ANCHO // 7, ALTO // 3), 5)
    pygame.draw.line(pantalla, AMARILLO, (6 * ANCHO // 7, 2 * ALTO // 3), (6 * ANCHO // 7, ALTO), 5)
    pygame.draw.line(pantalla, BLANCO, (0, ALTO // 2), (ANCHO // 28, ALTO // 2), 5)
    pygame.draw.line(pantalla, BLANCO, (2 * ANCHO // 28, ALTO // 2), (3 * ANCHO // 28, ALTO // 2), 5)
    pygame.draw.line(pantalla, BLANCO, (3 * ANCHO // 28, 7 * ALTO // 20), (4 * ANCHO // 28, 7 * ALTO // 20), 8)
    pygame.draw.line(pantalla, BLANCO, (3 * ANCHO // 28, 9 * ALTO // 20), (4 * ANCHO // 28, 9 * ALTO // 20), 8)
    pygame.draw.line(pantalla, BLANCO, (3 * ANCHO // 28, 11 * ALTO // 20), (4 * ANCHO // 28, 11 * ALTO // 20), 8)
    pygame.draw.line(pantalla, BLANCO, (3 * ANCHO // 28, 13 * ALTO // 20), (4 * ANCHO // 28, 13 * ALTO // 20), 8)
    pygame.draw.line(pantalla, BLANCO, (8 * ANCHO // 28, ALTO // 2), (9 * ANCHO // 28, ALTO // 2), 5)
    pygame.draw.line(pantalla, BLANCO, (10 * ANCHO // 28, ALTO // 2), (11 * ANCHO // 28, ALTO // 2), 5)
    pygame.draw.line(pantalla, BLANCO, (11 * ANCHO // 28, 7 * ALTO // 20), (12 * ANCHO // 28, 7 * ALTO // 20), 8)
    pygame.draw.line(pantalla, BLANCO, (11 * ANCHO // 28, 9 * ALTO // 20), (12 * ANCHO // 28, 9 * ALTO // 20), 8)
    pygame.draw.line(pantalla, BLANCO, (11 * ANCHO // 28, 11 * ALTO // 20), (12 * ANCHO // 28, 11 * ALTO // 20), 8)
    pygame.draw.line(pantalla, BLANCO, (11 * ANCHO // 28, 13 * ALTO // 20), (12 * ANCHO // 28, 13 * ALTO // 20), 8)
    pygame.draw.line(pantalla, BLANCO, (16 * ANCHO // 28, ALTO // 2), (17 * ANCHO // 28, ALTO // 2), 5)
    pygame.draw.line(pantalla, BLANCO, (18 * ANCHO // 28, ALTO // 2), (19 * ANCHO // 28, ALTO // 2), 5)
    pygame.draw.line(pantalla, BLANCO, (19 * ANCHO // 28, 7 * ALTO // 20), (20 * ANCHO // 28, 7 * ALTO // 20), 8)
    pygame.draw.line(pantalla, BLANCO, (19 * ANCHO // 28, 9 * ALTO // 20), (20 * ANCHO // 28, 9 * ALTO // 20), 8)
    pygame.draw.line(pantalla, BLANCO, (19 * ANCHO // 28, 11 * ALTO // 20), (20 * ANCHO // 28, 11 * ALTO // 20), 8)
    pygame.draw.line(pantalla, BLANCO, (19 * ANCHO // 28, 13 * ALTO // 20), (20 * ANCHO // 28, 13 * ALTO // 20), 8)
    pygame.draw.line(pantalla, BLANCO, (24 * ANCHO // 28, ALTO // 2), (25 * ANCHO // 28, ALTO // 2), 5)
    pygame.draw.line(pantalla, BLANCO, (26 * ANCHO // 28, ALTO // 2), (27 * ANCHO // 28, ALTO // 2), 5)
    pygame.draw.line(pantalla, BLANCO, (3 * ANCHO // 14, 0), (3 * ANCHO // 14, ALTO // 12), 5)
    pygame.draw.line(pantalla, BLANCO, (3 * ANCHO // 14, 2 * ALTO // 12), (3 * ANCHO // 14, 3 * ALTO // 12), 5)
    pygame.draw.line(pantalla, BLANCO, (9 * ANCHO // 56, 3 * ALTO // 12), (9 * ANCHO // 56, 4 * ALTO // 12), 8)
    pygame.draw.line(pantalla, BLANCO, (11 * ANCHO // 56, 3 * ALTO // 12), (11 * ANCHO // 56, 4 * ALTO // 12), 8)
    pygame.draw.line(pantalla, BLANCO, (13 * ANCHO // 56, 3 * ALTO // 12), (13 * ANCHO // 56, 4 * ALTO // 12), 8)
    pygame.draw.line(pantalla, BLANCO, (15 * ANCHO // 56, 3 * ALTO // 12), (15 * ANCHO // 56, 4 * ALTO // 12), 8)
    pygame.draw.line(pantalla, BLANCO, (3 * ANCHO // 14, 8 * ALTO // 12), (3 * ANCHO // 14, 9 * ALTO // 12), 5)
    pygame.draw.line(pantalla, BLANCO, (3 * ANCHO // 14, 10 * ALTO // 12), (3 * ANCHO // 14, 11 * ALTO // 12), 5)
    pygame.draw.line(pantalla, BLANCO, (7 * ANCHO // 14, ALTO // 12), (7 * ANCHO // 14, 2 * ALTO // 12), 5)
    pygame.draw.line(pantalla, BLANCO, (7 * ANCHO // 14, 3 * ALTO // 12), (7 * ANCHO // 14, 4 * ALTO // 12), 5)
    pygame.draw.line(pantalla, BLANCO, (25 * ANCHO // 56, 8 * ALTO // 12), (25 * ANCHO // 56, 9 * ALTO // 12), 8)
    pygame.draw.line(pantalla, BLANCO, (27 * ANCHO // 56, 8 * ALTO // 12), (27 * ANCHO // 56, 9 * ALTO // 12), 8)
    pygame.draw.line(pantalla, BLANCO, (29 * ANCHO // 56, 8 * ALTO // 12), (29 * ANCHO // 56, 9 * ALTO // 12), 8)
    pygame.draw.line(pantalla, BLANCO, (31 * ANCHO // 56, 8 * ALTO // 12), (31 * ANCHO // 56, 9 * ALTO // 12), 8)
    pygame.draw.line(pantalla, BLANCO, (7 * ANCHO // 14, 9 * ALTO // 12), (7 * ANCHO // 14, 10 * ALTO // 12), 5)
    pygame.draw.line(pantalla, BLANCO, (7 * ANCHO // 14, 11 * ALTO // 12), (7 * ANCHO // 14, ALTO), 5)
    pygame.draw.line(pantalla, BLANCO, (11 * ANCHO // 14, 0), (11 * ANCHO // 14, ALTO // 12), 5)
    pygame.draw.line(pantalla, BLANCO, (11 * ANCHO // 14, 2 * ALTO // 12), (11 * ANCHO // 14, 3 * ALTO // 12), 5)
    pygame.draw.line(pantalla, BLANCO, (41 * ANCHO // 56, 3 * ALTO // 12), (41 * ANCHO // 56, 4 * ALTO // 12), 8)
    pygame.draw.line(pantalla, BLANCO, (43 * ANCHO // 56, 3 * ALTO // 12), (43 * ANCHO // 56, 4 * ALTO // 12), 8)
    pygame.draw.line(pantalla, BLANCO, (45 * ANCHO // 56, 3 * ALTO // 12), (45 * ANCHO // 56, 4 * ALTO // 12), 8)
    pygame.draw.line(pantalla, BLANCO, (47 * ANCHO // 56, 3 * ALTO // 12), (47 * ANCHO // 56, 4 * ALTO // 12), 8)
    pygame.draw.line(pantalla, BLANCO, (11 * ANCHO // 14, 8 * ALTO // 12), (11 * ANCHO // 14, 9 * ALTO // 12), 5)
    pygame.draw.line(pantalla, BLANCO, (11 * ANCHO // 14, 10 * ALTO // 12), (11 * ANCHO // 14, 11 * ALTO // 12), 5)
    pygame.draw.line(pantalla, AMARILLO, (0, 2 * ALTO // 3), (ANCHO // 7, 2 * ALTO // 3), 5)
    pygame.draw.line(pantalla, AMARILLO, (2 * ANCHO // 7, 2 * ALTO // 3), (3 * ANCHO // 7, 2 * ALTO // 3), 5)
    pygame.draw.line(pantalla, AMARILLO, (4 * ANCHO // 7, 2 * ALTO // 3), (5 * ANCHO // 7, 2 * ALTO // 3), 5)
    pygame.draw.line(pantalla, AMARILLO, (6 * ANCHO // 7, 2 * ALTO // 3), (ANCHO, 2 * ALTO // 3), 5)

    # Dibujar semáforos
    semaforo_1.dibujar_horizontal(pantalla)
    semaforo_2.dibujar_horizontal(pantalla)
    semaforo_3.dibujar_horizontal(pantalla)
    semaforo_4.dibujar_vertical_inferior(pantalla)
    semaforo_5.dibujar_vertical(pantalla)
    semaforo_6.dibujar_vertical_inferior(pantalla)

    # Dibujar botón de salir
    pygame.draw.rect(pantalla, (255, 0, 0), boton_salir)
    fuente = pygame.font.SysFont(None, 24)
    texto = fuente.render("Salir", True, (255, 255, 255))
    pantalla.blit(texto, (715, 17))

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización
    reloj.tick(60)

# Cerrar pygame
pygame.quit()
