class Player:
    def __init__(self):
        self.name = ''
        self.age = 0

player1 = Player()
# player2 = Player()


def player_name():
    q1p1 = input(str('What is your name bruuhhh...\n'))
    # q1p2 = input(str('What is your name bruuhhh...\n'))

    player1.name = q1p1
    # player2.name = q1p2

def player_age():
    q2p1 = input('How old are you champ...\n')
    # q2p2 = input('How old are you champ...\n')

    player1.age = q2p1
    # player2.age = q2p2

#start programme
player_name()
player_age()
print(player1.name,'\n',player1.age)
# print(player2.age,'\n',player2.name)


# class Player:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def player_name(self):
#         name = input(str('Choose Your Name...'))
    

#     def player_age(self):
#     #needs to add in str or int 
#     #look up in automate book 
#         age = input('How old are you...')
    

# player_1 = Player()
# print(player_1.name)

# name.player_name()
# age.player_age()
# print(player_1.name)
