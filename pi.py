import math
import random
import pygame
pygame.font.init()

win = pygame.display.set_mode((500,700))
run = True
font = pygame.font.SysFont('arial', 30)
font1 = pygame.font.SysFont('arial', 20)
font2 = pygame.font.SysFont('arial', 15)

center = (1,1)
radius = 1
circle = 0
square = 0
points = []
clicked = True
PI = 0
used = 10000
f = 10000
toUse = 10000
regenerate = pygame.Rect(15,580,150,60)
up = pygame.Rect(195,580,100,60)
down = pygame.Rect(320,580,100,60)
# circle area = PI*r^2
# square area = d^2 or 2r^2
# PI : 4
# circle/square = PI/4
# square*PI = 4*circle
#PI = (4*circle)/square

def genPoints(n):
    global square,circle,used,points
    square = 0
    circle = 0
    points = []
    print("cleared")
    for i in range(n):
        point = (random.uniform(0,2),random.uniform(0,2))
        points.append(point)
        if math.dist(point,center) < 1:
            circle += 1
        square += 1
    used = n

def getPI():
    global PI
    PI = (4*circle)/square
    print(PI)

genPoints(10000)
getPI()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if pygame.mouse.get_pressed()[0]:
        clicked = True
    if pygame.mouse.get_pressed()[0] == False and clicked:
        pos = pygame.mouse.get_pos()
        if regenerate.collidepoint(pos):
            genPoints(toUse)
            getPI()
        if up.collidepoint(pos):
            toUse += 1000
        if down.collidepoint(pos) and toUse >= 2000:
            toUse -= 1000
        clicked = False
    text = font.render(f"Estimated value of Pi: {PI}", False, (255,0,255))
    text2 = font1.render(f"Amount of points used for determination {used}", False, (255,0,255))
    text3 = font1.render(f"Regenerate", False, (0,0,0))
    text4 = font1.render(f"points", False, (0,0,0))
    text5 = font1.render(f"Points to use for next generation: {toUse}", False, (255,0,255))
    text6 = font2.render(f"Raise points", False, (0,0,0))
    text7 = font2.render(f"Lower points", False, (0,0,0))
    win.fill((0,0,0))
    win.blit(text,(10,515))
    win.blit(text2,(10,550))
    pygame.draw.circle(win,(255,255,255),(250,250),250,1)
    pygame.draw.rect(win,(255,0,255),regenerate)
    pygame.draw.rect(win,(255,0,255),up)
    pygame.draw.rect(win,(255,0,255),down)
    win.blit(text4,(60,605))
    win.blit(text3,(35,585))
    win.blit(text5,(20,650))
    win.blit(text6,(203,600))
    win.blit(text7,(330,600))
    if points:
        for point in points:
            pygame.draw.circle(win,(255,255,255),(point[0]*250,500-point[1]*250),1)
    pygame.display.update()

