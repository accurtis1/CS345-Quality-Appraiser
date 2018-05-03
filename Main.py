import pygame
from Mechanism import Mechanism

pygame.init()
pygame.event.pump()

mech = Mechanism()
mech.render_display()

pressedButton = None

def event_loop():
    while True:
        for event in pygame.event.get():
            #Mouse click
            if event.type == 5:
                pressedButton = mech.press_and_get_button( pygame.mouse.get_pos() )
            #Mouse release
            if event.type == 6:
                mech.release_button( pressedButton )
                mech.execute_event( pressedButton, mech.eventDict )
                pressedButton = None

event_loop()
