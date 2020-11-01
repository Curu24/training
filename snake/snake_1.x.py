import pygame
from pygame import mixer
import random

pygame.init()

#Caption and icon
screen = pygame.display.set_mode((400, 680))
pygame.display.set_caption("Snake v1.2")
icon = pygame.image.load("snake.png")
pygame.display.set_icon(icon)

#Snake
simg = pygame.image.load("snk.png")
hx = 200
hy = 300
speed = 1
body = [(200, 300)]
def snake():
    for element in body:
        screen.blit(simg, (element))
def head():
    screen.blit(simg, (hx, hy))

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
        if (hx%20 == 0) and (hy%20 == 0):
            if movement == "left":
                if (hx-20 < 0) or (hx-20, hy) in body:
                    state = "game_over"
                    mixer.music.load("zapThreeToneDown.mp3")
                    mixer.music.play(1)
                elif hx == dx and hy == dy:
                    body.append((hx, hy))
                    score += 1
                    mixer.music.load("phaserUp4.mp3")
                    mixer.music.play(1)
                    while True:
                        dx = random.randrange(0, 400, 20)
                        dy = random.randrange(0, 600, 20)
                        if not (dx, dy) in body:
                            break
                else:
                    body.append((hx, hy))
                    body.pop(0)
                direction = "left"
                hx -= speed
            if movement == "right":
                if (hx+20 > 380) or (hx+20, hy) in body:
                    state = "game_over"
                    mixer.music.load("zapThreeToneDown.mp3")
                    mixer.music.play(1)
                elif hx == dx and hy == dy:
                    body.append((hx, hy))
                    score += 1
                    mixer.music.load("phaserUp4.mp3")
                    mixer.music.play(1)
                    while True:
                        dx = random.randrange(0, 400, 20)
                        dy = random.randrange(0, 600, 20)
                        if not (dx, dy) in body:
                            break
                else:
                    body.append((hx, hy))
                    body.pop(0)
                direction = "right"
                hx += speed
            if movement == "up":
                if (hy-20 < 0) or (hx, hy-20) in body:
                    state = "game_over"
                    mixer.music.load("zapThreeToneDown.mp3")
                    mixer.music.play(1)
                elif hx == dx and hy == dy:
                    body.append((hx, hy))
                    score += 1
                    mixer.music.load("phaserUp4.mp3")
                    mixer.music.play(1)
                    while True:
                        dx = random.randrange(0, 400, 20)
                        dy = random.randrange(0, 600, 20)
                        if not (dx, dy) in body:
                            break
                else:
                    body.append((hx, hy))
                    body.pop(0)
                direction = "up"
                hy -= speed
            if movement == "down":
                if (hy+20 > 580) or (hx, hy+20) in body:
                    state = "game_over"
                    mixer.music.load("zapThreeToneDown.mp3")
                    mixer.music.play(1)
                elif hx == dx and hy == dy:
                    body.append((hx, hy))
                    score += 1
                    mixer.music.load("phaserUp4.mp3")
                    mixer.music.play(1)
                    while True:
                        dx = random.randrange(0, 400, 20)
                        dy = random.randrange(0, 600, 20)
                        if not (dx, dy) in body:
                            break
                else:
                    body.append((hx, hy))
                    body.pop(0)
                direction = "down"
                hy += speed

        else:
            if direction == "left":
                hx -= speed
            if direction == "right":
                hx += speed
            if direction == "up":
                hy -= speed
            if direction == "down":
                hy += speed

        snake()
        head()
        dot(dx, dy)
        showscore(10, 600)
        pygame.time.wait(8)

    elif state == "game_over":
        gover = font2.render("GAME OVER!" , True, (255, 255, 255))
        screen.blit(gover, (40, 250))
        showscore(10, 600)

    pygame.display.update()
