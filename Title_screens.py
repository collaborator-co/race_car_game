import cmd
import time
import math
import os
import sys
import win32api
import time

one = win32api.GetKeyState(0x31)
two = win32api.GetKeyState(0x32)
three = win32api.GetKeyState(0x33)
four = win32api.GetKeyState(0x34)
five = win32api.GetKeyState(0x35)
six = win32api.GetKeyState(0x36)
seven = win32api.GetKeyState(0x37)
eight = win32api.GetKeyState(0x38)
nine =  win32api.GetKeyState(0x39)
zero = win32api.GetKeyState(0x30)
w_key = win32api.GetKeyState(0x57)
s_key = win32api.GetKeyState(0x53)
a_key = win32api.GetKeyState(0x41)
d_key = win32api.GetKeyState(0x44)
space_key =win32api.GetKeyState(0x20)
q_key = win32api.GetKeyState(0x51)


# insert a loading bar screen 
# and loading bar function to callbetween screens

def title_screen():
    
    print('''
    ############################
    ############################
    ###     --Race-Day--     ###
    ###                      ###
    ###   -Press Space Bar-  ###
    ###                      ###
    ###                      ###   
    ############################
    ############################
    ''')
    
        
    

def select_laguage():
    
    print('''
    ############################
    ############################
    ###     --Race-Day--     ###
    ###                      ###
    ###  -Select  language-  ###
    ### [1]ENG [2]CHI [3]FRA ###
    ###                      ###   
    ############################
    ############################
    ''')
    


def player_mode():
    # os.system('clear')
    print('''
    ############################
    ############################
    ###     --Race-Day--     ###
    ###                      ###
    ###   -Single player-    ###
    ###     -Vs Battle-      ###
    ###                      ###   
    ############################
    ############################
    ''')

def player_name():
    os.system('clear')
    print('''
    ############################
    ############################
    ###     --Race-Day--     ###
    ###   enter name _ _ _   ###
    ###   A B C D E F G H I  ###
    ###   J K L M N O P Q R  ###
    ###   S T U V W X Y Z >  ###   
    ############################
    ############################
    ''')

def main_menu():
    os.system('clear')
    print('''
    ############################
    ############################
    ###     --Race-Day--     ###
    ###       -Random-       ###
    ###        -Track-       ###
    ###         -Car-        ###
    ###                      ###   
    ############################
    ############################
    ''')

# def any_key():
#     if input() == str or int:
#         select_laguage()


# title_screen()
# while True:

#     space_bar = space_key
#     if space_bar < 0:
    
#         select_laguage()
#         break
#     time.sleep(0.1)        

# any_key()
# player_mode()
# player_name()
# main_menu()


#player info and stats 

