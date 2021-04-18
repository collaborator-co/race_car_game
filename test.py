# import win32api
import time
import Title_screens
from pynput import keyboard

# while True:
#     a = win32api.GetKeyState(0x57)
#     if a < 0:
#         print('A Key is pressed!!')
#         break
#     time.sleep(0.5)
# start game 
# run title 

#  Loading bar sequence 
# Title_screens.title_screen()
# while True:

#     # space_bar = space_key
#     if Title_screens.space_key < 0:
#         Title_screens.select_laguage()
#         break      

# from pynput import keyboard

# The event listener will be running in this block
with keyboard.Events() as events:
    # Block at most one second
    event = events.get()
    if event is '1':
        
    else:
        print('Received event {}'.format(event))
