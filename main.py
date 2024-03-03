import pgzrun
import random

TITLE = "Alien Shooter"
WIDTH = 500
HEIGHT = 500
message = ""
#actors = objects
alien = Actor("alien")
alien.pos = 250,250

def draw():
    global message
    screen.clear()
    screen.fill(color=(201,213,181))
    alien.draw()
    screen.draw.text(message, fontsize=30, center=(250,40))

def randpos():
    x = random.randint(50, WIDTH - 50)
    y = random.randint(50, HEIGHT - 50)
    alien.x = x
    alien.y = y

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message = "Great Shot!"
        randpos()
    else:
        message = "Missed it!"

randpos()

pgzrun.go()