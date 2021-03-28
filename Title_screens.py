import cmd
import time
import math
import os
import sys

def title_screen():
    os.system('clear')
    print('''
    ############################
    ############################
    ###     --Race-Day--     ###
    ###                      ###
    ###   -Press any Key-    ###
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
    ###                      ###
    ###                      ###   
    ############################
    ############################
    ''')


def player_mode():
    os.system('clear')
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




title_screen()
player_mode()
player_name()
main_menu()


#player info and stats 



