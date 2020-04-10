from sense_hat import SenseHat
import time
import datetime
import pygame
from pygame.locals import *


sense = SenseHat()
sense.clear()
sense.set_rotation(r=90)

pygame.init()
pygame.display.set_mode((640,480))

pressure = 'P: ' + str(int(sense.get_pressure()))
temp =  'T: ' + str(int(sense.get_temperature_from_pressure()))
humidity = 'H: ' + str(int(sense.get_humidity()))
blah = 'blah!'

def handle_event(event):
    if event.key == pygame.K_DOWN:
        sense.show_message(pressure)
    elif event.key == pygame.K_UP:
        sense.show_message(temp)
    elif event.key == pygame.K_LEFT:
        sense.show_message(humidity)
    elif event.key == pygame.K_RIGHT:
        sense.show_message(blah)       


running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            handle_event(event)
        if event.type == KEYUP:
            handle_event(event)
        if event.type == K_ESCAPE:
            running = False
        if event.type == pygame.QUIT:
            running = False
