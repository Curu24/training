import pygame
import random

pygame.init()

#Caption and icon
screen = pygame.display.set_mode((400, 680))
pygame.display.set_caption("Snake v1.0")
icon = pygame.image.load("snake.png")
pygame.display.set_icon(icon)

#Snake
simg = pygame.image.load("snk.png")
sx = 200
sy = 300
body = [(sx, sy)]
def snake():
    for element in body:
        screen.blit(simg, (element))

#Dot
dimg = pygame.image.load("dot.png")
dx = random.randrange(0, 400, 20)
dy = random.randrange(0, 600, 20)
def dot(dx, dy):
    screen.blit(dimg, (dx, dy))

#Score
score = 0
font1 = pygame.font.Font("arcade.ttf", 40)
font2 = pygame.font.Font("arcade.ttf", 70)
def showscore(x, y):
    scimg = pygame.image.load("line.png")
    screen.blit(scimg, (x, y))
    scr = font1.render("SCORE:                        " + str(score), True, (255, 255, 255))
    screen.blit(scr, (x+10, y+20))

state = "play"
movement = "no"

running = True
while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movement = "left"

            if event.key == pygame.K_RIGHT:
                movement = "right"

            if event.key == pygame.K_UP:
                movement = "up"

            if event.key == pygame.K_DOWN:
                movement = "down"

    if state == "play":
        if movement == "left":
            if (sx-20 < 0) or (sx-20, sy) in body:
                state = "game_over"
            elif sx-20 == dx and sy == dy:
                sx -= 20
                body.append((sx, sy))
                score += 1
                while True:
                    dx = random.randrange(0, 400, 20)
                    dy = random.randrange(0, 600, 20)
                    if not (dx, dy) in body:
                        break
                pygame.time.wait(250)
            else:
                sx -= 20
                body.append((sx, sy))
                body.pop(0)
                pygame.time.wait(250)
        if movement == "right":
            if (sx+20 > 380) or (sx+20, sy) in body:
                state = "game_over"
            elif sx+20 == dx and sy == dy:
                sx += 20
                body.append((sx, sy))
                score += 1
                while True:
                    dx = random.randrange(0, 400, 20)
                    dy = random.randrange(0, 600, 20)
                    if not (dx, dy) in body:
                        break
                pygame.time.wait(250)
            else:
                sx += 20
                body.append((sx, sy))
                body.pop(0)
                pygame.time.wait(250)
        if movement == "up":
            if (sy-20 < 0) or (sx, sy-20) in body:
                state = "game_over"
            elif sx == dx and sy-20 == dy:
                sy -= 20
                body.append((sx, sy))
                score += 1
                while True:
                    dx = random.randrange(0, 400, 20)
                    dy = random.randrange(0, 600, 20)
                    if not (dx, dy) in body:
                        break
                pygame.time.wait(250)
            else:
                sy -= 20
                body.append((sx, sy))
                body.pop(0)
                pygame.time.wait(250)
        if movement == "down":
            if (sy+20 > 580) or (sx, sy+20) in body:
                state = "game_over"
            elif sx == dx and sy+20 == dy:
                sy += 20
                body.append((sx, sy))
                score += 1
                while True:
                    dx = random.randrange(0, 400, 20)
                    dy = random.randrange(0, 600, 20)
                    if not (dx, dy) in body:
                        break
                pygame.time.wait(250)
            else:
                sy += 20
                body.append((sx, sy))
                body.pop(0)
                pygame.time.wait(250)

        snake()
        dot(dx, dy)
        showscore(10, 600)

    elif state == "game_over":
        gover = font2.render("GAME OVER!" , True, (255, 255, 255))
        screen.blit(gover, (40, 250))
        showscore(10, 600)

    pygame.display.update()
