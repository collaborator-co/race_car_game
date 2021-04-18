import sys
import os
import time
import win32api

class Cars:
    def __init__ (self):
        self.colour = ''
        self.speed = 0.0
        self.mpg = 0.0
        self.fuel = 0.0
        self.weight = 0.0

player_car = Cars()


def car_choice():
    print('''
             ##########################################
             ##########################################
             ######                              ######
             ######     -Pick a colour car-      ######
             ######                              ######
             ######            [1] Blue          ######
             ######            [2] Green         ######
             ######            [3] Red           ###### 
             ######   [h+1,2 or 3] View Stats    ######
             ######                              ######
             ##########################################
             ##########################################''')

    while True:

        global blue 
        blue =  win32api.GetKeyState(0x31) # key 1
        global green 
        green =  win32api.GetKeyState(0x32)  # Key 2
        global red 
        red =  win32api.GetKeyState(0x33)  # Key 3
        h =  win32api.GetKeyState(0x48) 

        if blue < 0:
            os.system('cls')
            time.sleep(1)
            # loading bar 
            print('''
                ##########################################
                ##########################################
                ######                              ######
                ######     -You Picked Colour-      ######
                ######                              ######
                ######             Blue             ######
                ######                              ######
                ######                              ######
                ######                              ######
                ######                              ######
                ##########################################
                ##########################################''')
            time.sleep(1)
            # add stats to class from here
            break
            

        elif green < 0:
            os.system('cls')
            time.sleep(1)
            print('''
                ##########################################
                ##########################################
                ######                              ######
                ######     -You Picked Colour-      ######
                ######                              ######
                ######             Green            ######
                ######                              ######
                ######                              ######
                ######                              ######
                ######                              ######
                ##########################################
                ##########################################''')
            time.sleep(1)
            break
            
        # sleep.time()  count down from 10 then continue to next selection screen
        # continue (next screen )

        elif red < 0:
            os.system('cls')
            time.sleep(1)
            print('''
                ##########################################
                ##########################################
                ######                              ######
                ######     -You Picked Colour-      ######
                ######                              ######
                ######             Red              ######
                ######                              ######
                ######                              ######
                ######                              ######
                ######                              ######
                ##########################################
                ##########################################''')
            time.sleep(0.5)
            break
            

        elif h < 0 and blue < 0:
            print('''
                ##########################################
                ##########################################
                ######                              ######
                ######         -Blue Stats-         ######
                ######                              ######
                ######          Speed               ######
                ######          MPG                 ######
                ######          Fuel                ######
                ######          Weight              ######
                ######                              ######
                ##########################################
                ##########################################''')
            return car_choice()

        elif h < 0 and green < 0:
            print('''
                ##########################################
                ##########################################
                ######                              ######
                ######         -Green Stats-        ######
                ######                              ######
                ######          Speed               ######
                ######          MPG                 ######
                ######          Fuel                ######
                ######          Weight              ######
                ######                              ######
                ##########################################
                ##########################################''')
            return car_choice()

        elif h < 0 and red < 0:
            print('''
                ##########################################
                ##########################################
                ######                              ######
                ######         -Red Stats-          ######
                ######                              ######
                ######          Speed               ######
                ######          MPG                 ######
                ######          Fuel                ######
                ######          Weight              ######
                ######                              ######
                ##########################################
                ##########################################''')
            time.sleep(1)
            return car_choice()
        # time.sleep(1)    
        
        
       

            

         




             
    
    
    
    
    
    # colour_view = input('To view colours input v ..\n')
    # if colour_view == 'v':
    #     print('blue','\ngreen','\nred')
    # print('Would you like to view the cars base stats???\n')
    
    
    # stats_view1 = input('Y...or...N')
    # while stats_view1 == 'Y':
    
    #     print('Which colour would you like to view???','\n\nTo exit press N...')
    #     print('  blue  ','\n\n  green  ','\n\n  red  ')
        
    #     user_colour = input('>>>')
    #     if user_colour == "blue":
    #         print('speed = 50','\nmpg = 45','\nfuel = 60','\nweight = 800')
    #     elif user_colour == "green":
    #         print('speed = 60','\nmpg = 40','\nfuel = 60','\nweight = 750')
    #     elif user_colour == "red":
    #         print('speed = 40','\nmpg = 35','\nfuel = 60','\nweight = 900')
    #     else:
    #         break


    
    # elif stats_view1 == 'N':
        
    # car_colour = input(str('Pick a colour car...'))
    # player_car.colour = car_colour

car_choice()



# if car_choice == blue:
    
#     player_car.speed = 50,
#     player_car.mpg = 45,
#     player_car.fuel = 60,
#     player_car.weight = 800,

# elif car_choice() == green:
    
#     player_car.speed = 60,
#     player_car.mpg = 40,
#     player_car.fuel = 60,
#     player_car.weight = 750,

# elif car_choice() == red:
    
#     player_car.speed = 40,
#     player_car.mpg = 35,
#     player_car.fuel = 60,
#     player_car.weight = 950,

# else:
#     print('Sorry that was not valid!!!')
#     car_choice()

# print(player_car.speed)


# print(player_car.colour)



#car colour choice selceted in player programme

# Car speed atributes define by colour choice alter game play stats 
# quicker you look search faster fuel goes 
# in game mechanics 