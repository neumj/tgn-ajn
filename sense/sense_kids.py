from sense_hat import SenseHat
import time
import numpy
#import datetime
#import pygame
#from pygame.locals import *

#set uo stuff
sense = SenseHat()
sense.clear()
sense.set_rotation(180)


#function
def get_temp(samples):
    ts = []
    for i in range(0,samples):
        t = sense.get_temperature()
        ts.append(t)
        time.sleep(0.25)
    ave_t = sum(ts) / float(samples)
    return str(ave_t)
        #txt = get_temp(10)
        #sense.show_message(txt.upper(),scroll_speed=0.15,back_colour=[50,0,100])
    

def check_time():
    nw = time.localtime()
    if nw.tm_hour >= 6 and nw.tm_hour < 12:
        return ' good morning!'
    elif nw.tm_hour >= 12 and nw.tm_hour < 17:
        return ' good afternoon!'
    elif nw.tm_hour >= 17 and nw.tm_hour < 19:
        return ' good evening!'
    elif nw.tm_hour > 19:
        return ' time to go to sleep.'
        #txt = check_time()
        #sense.show_message(txt.upper(),scroll_speed=0.15,back_colour=[50,0,100])


def green_pixel(xpos,ypos):
    sense.set_pixel(xpos,ypos,0,255,0)

def red_pixel(xpos,ypos):
    sense.set_pixel(xpos,ypos,255,0,0)
        
def fill_matrix(count):
    sense.clear()
    abs_count = abs(count)
    row = 0
    col = 0
    for i in range(0,abs_count):
        if count < 0:
            red_pixel(col,row)
        elif count > 0:
            green_pixel(col,row)
        elif count == 0:
            sense.clear()
        col += 1
        if col == 8:
            row += 1
            col =0
        
running = True

pt_count = 0
while running:
    event = sense.stick.wait_for_event()
    if event.direction == 'up' and event.action == 'pressed':        
        pt_count += -1
    elif event.direction == 'down' and event.action == 'pressed':
        pt_count += 1
    time.sleep(0.25)    
    fill_matrix(pt_count)    
    if pt_count < -64:
        running = False
    if pt_count > 64:
        running = False
        
    