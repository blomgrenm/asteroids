import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,5)
        self.velocity = 0

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt
        # super().velocity