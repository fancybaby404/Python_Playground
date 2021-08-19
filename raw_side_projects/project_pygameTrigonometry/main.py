import math

import pygame
import pygame.gfxdraw


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.radius = 100
        self.angle = 0
        self.image = pygame.Surface([1, 1])
        self.rect = self.image.get_rect()

    def spin_circle(self):
        self.angle += 1
        self.rect.centerx = math.cos(math.radians(self.angle)) * self.radius + 250
        self.rect.centery = math.sin(math.radians(self.angle)) * self.radius + 250

        if self.angle >= 360:
            self.angle = 0

    def update(self):
        pygame.gfxdraw.aacircle(display, self.rect.x, self.rect.y, 20, (255, 165, 0))
        pygame.gfxdraw.filled_circle(display, self.rect.x, self.rect.y, 20, (255, 165, 0))
        self.spin_circle()


pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode((500, 500))

# -------- Ball
ball = pygame.sprite.GroupSingle()
ball.add(Ball())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    display.fill('White')

    ball.draw(display)
    ball.update()

    clock.tick(144)
    pygame.display.update()
