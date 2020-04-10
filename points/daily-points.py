# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 22:08:03 2019

@author: pi
"""

from sense_hat import SenseHat
import time
#import numpy


sense = SenseHat()
sense.clear()
sense.set_rotation(180)

def set_bar_color(row,col,color):
    #loops across a row and sets pixels to a color
    for i in range(0,col):
        sense.set_pixel(i,row,color[0],color[1],color[2])
        
def green_pixel(xpos,ypos):
    sense.set_pixel(xpos,ypos,0,255,0)

def red_pixel(xpos,ypos):
    sense.set_pixel(xpos,ypos,255,0,0)

def gold_pixel(xpos,ypos):
    sense.set_pixel(xpos,ypos,255,213,0)
        
def get_hour():
    nw = time.localtime()
    return nw.tm_hour

def rows_by_hour(hour):
    if hour >= 0 and hour < 11:
        rows = [1,5]
    elif hour >= 11 and hour < 18:
        rows = [2,6]
    elif hour >= 18 and hour < 24:
        rows = [3,7]
    return rows        

def fill_row(row,count):
    abs_count = abs(count)
    if abs_count > 7:
        abs_count = 8
    col = 0
    set_bar_color(row,8,[0,0,0])
    for i in range(0,abs_count):
        if count < 0:
            red_pixel(col,row)
        elif count > 0 and count < 8:
            green_pixel(col,row)
        elif count >= 8:
            gold_pixel(col,row)
        elif count == 0:
            sense.set_pixel(col,row,0,0,0)
        col += 1
        
#player info
player = {0:{'active_color':[0,0,255],
             'inactive_color':[0,0,50],
             'points': 0},
          1:{'active_color':[180,0,150],
             'inactive_color':[155,100,0],
             'points': 0}
         }

#setup             
running = True
set_bar_color(0,8,player[0]['active_color'])
set_bar_color(4,4,player[1]['active_color'])
active_player = 0

while running:
    event = sense.stick.wait_for_event()
    #active player
    if event.direction == 'up' and event.action == 'pressed':
        set_bar_color(0,8,[0,0,0])
        set_bar_color(4,8,[0,0,0])
        set_bar_color(0,4,player[0]['active_color'])
        set_bar_color(4,8,player[1]['active_color'])
        active_player = 1
    elif event.direction == 'down' and event.action == 'pressed':
        set_bar_color(0,8,[0,0,0])
        set_bar_color(4,8,[0,0,0])
        set_bar_color(0,8,player[0]['active_color'])
        set_bar_color(4,4,player[1]['active_color'])
        active_player = 0

    #points
    if event.direction == 'right' and event.action == 'pressed':
        player[active_player]['points'] += -1
        fill_rows = rows_by_hour(get_hour())
        fill_row(fill_rows[active_player],player[active_player]['points'])
    elif event.direction == 'left' and event.action == 'pressed':
        player[active_player]['points'] += 1
        fill_rows = rows_by_hour(get_hour())
        fill_row(fill_rows[active_player],player[active_player]['points'])
      
    #clear ad stop
    if event.direction == 'middle' and event.action == 'held':
        sense.clear()
        running = False