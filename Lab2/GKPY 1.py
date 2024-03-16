'Zadanie 1'
import pygame
import sys
import math

pygame.init()

width, height = 600, 600
screen = pygame.display.set_mode((width, height))
white = (255, 255, 255)
black = (0, 0, 0)
cenx, ceny = 300,300

'powierzchnie'
surfaceorg = pygame.Surface((2*cenx, 2*ceny))
surnex = pygame.Surface((2*cenx, 2*ceny))
surnex2 = pygame.Surface((2*cenx, 2*ceny))

'wielokąt'
num_sides = 18
radius = 150
vertices = []
for i in range(num_sides):
    angle = (2 * math.pi * i) / num_sides
    x = cenx + int(radius * math.cos(angle))
    y = ceny + int(radius * math.sin(angle))
    vertices.append((x, y))

def draw_polygon(vertices):
    pygame.draw.polygon(surfaceorg, white, vertices, 2)



running = True
while running:
    
    draw_polygon(vertices)
    surnex2.blit(pygame.transform.rotozoom(surfaceorg,45,1.2),(-210,-210))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                screen.fill(black)
                screen.blit(pygame.transform.rotozoom(surfaceorg,45,1.2),(-210,-210))
                pygame.display.flip()
                
            if event.key == pygame.K_2:
                screen.fill(black)
                screen.blit(surfaceorg, (0, 0))
                pygame.display.flip()
            if event.key == pygame.K_3:
                screen.fill(black)
                screen.blit(pygame.transform.flip(pygame.transform.scale_by(surnex2,(1,1.2)),False,True),(0,0))
                pygame.display.flip()
            if event.key == pygame.K_4:
                screen.fill(black)
                surnex.blit(pygame.transform.scale_by(surfaceorg,(2,1)),(-300,-150))
                screen.blit(pygame.transform.rotozoom(surnex,153,0.6),(100,00))
                pygame.display.flip()
            if event.key == pygame.K_5:
                screen.fill(black)
                screen.blit(pygame.transform.scale_by(surnex2,(2,1)),(-300,-150))
                pygame.display.flip()
            if event.key == pygame.K_6:
                screen.fill(black)
                surnex.blit(pygame.transform.scale_by(surfaceorg,(2,1)),(-300,-150))
                screen.blit(pygame.transform.rotozoom(surnex,63,0.8),(100,00))
                pygame.display.flip()
            if event.key == pygame.K_7:
                screen.fill(black)
                screen.blit(pygame.transform.flip(pygame.transform.scale_by(surnex2,(1,1.2)),True,True),(0,0))
                pygame.display.flip()
            if event.key == pygame.K_8:
                screen.fill(black)
                surnex2.blit(pygame.transform.scale_by(surnex2,(2,1)),(-300,-150))
                screen.blit(pygame.transform.rotozoom(surnex,150,0.6),(0,100))
                pygame.display.flip()
            if event.key == pygame.K_9:
                screen.fill(black)
                surnex.blit(pygame.transform.scale_by(surfaceorg,(2,1)),(-300,-150))
                screen.blit(pygame.transform.rotozoom(surnex,-63,0.8),(-60,00))
                pygame.display.flip()
            
            
pygame.quit()
sys.exit()
