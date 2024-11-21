import pygame

from pygame import Color, Rect
from pygame import draw
from pygame import display

SCREEN_SIZE = (500, 500)


pygame.init()


gameDisplay = display.set_mode(SCREEN_SIZE)


gameDisplay.fill(Color('darkblue'))


draw.rect(gameDisplay, Color('brown'), Rect(275, 250, 50, 150))
draw.polygon(gameDisplay, Color('darkgreen'), [(185, 285), (415, 285), (300, 50)])

draw.circle(gameDisplay, Color('grey'), (75, 75), 50)

draw.circle(gameDisplay, Color('darkgrey'), (73, 68), 10)

draw.circle(gameDisplay, Color('darkgrey'), (43, 50), 10)

draw.circle(gameDisplay, Color('darkgrey'), (82, 90), 10)


display.flip()


input("Press enter to exit")