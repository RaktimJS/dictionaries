# Last edited on 30/12/2024

import module
import time

from os import system
from pack import pack

def timer(s):
        while s: 
                time.sleep(1)
                s -= 1




pack('interface.py', True)

system('cls')

continuationSelector = ''

while True:
        if continuationSelector == 'cls' or continuationSelector == '':
                print("\n\n\nO P E R A T I O N S   U S I N G   A N D   O N   D I C T I O N A R I E S")
                print("-----------------------------------------------------------------------\n")

                print("Enter \033[38;2;255;165;0m1\033[38;2;212;212;212m → GUESS THE KEY IN A DICTIONARY GAME")
                print("Enter \033[38;2;255;165;0m2\033[38;2;212;212;212m → FIND SQUARES FROM 1 TO n AS A DICTIONARY")
                print("Enter \033[38;2;255;165;0m3\033[38;2;212;212;212m → FINDING NUMBER OF APPEARENCES OF ALL CHARACTERS IN A STRING")
                print("Enter \033[38;2;255;165;0m4\033[38;2;212;212;212m → UPDATE ELEMENTS IN A LIST VALUE IN A DICTIONARY")
                print("Enter \033[38;2;255;165;0m5\033[38;2;212;212;212m → FIND KEY HAVING MINIMUM AND MAXIMUM VALUES IN A DICTIONARY")

        listSelector = input("\n\nEnter a selection from the above list: \033[38;2;255;165;0m")
        print("\033[38;2;212;212;212m", end="")
        print("------------------------------------------------------------------------------\n\n\n")

# CHOOSE FUNCTION BY INPUT
        try:
                listSelector = int(listSelector)

                if listSelector == 1:
                        module.isKeyAvailable()
                elif listSelector == 2:
                        module.squares()
                elif listSelector == 3:
                        module.charCounter()
                elif listSelector == 4:
                        module.updateElement()
                elif listSelector == 5:
                        module.minMaxFetcher()
                elif listSelector < 1:
                        print("Input out of range. Setting it to closest limit")
                        module.isKeyAvailable()
                elif listSelector > 5:
                        print("Input out of range. Setting it to closest limit")
                        module.minMaxFetcher()
                else:
                        print("An unexpected error occured")
                
                print("------------------------------------------------------------------------------\n\n\n")
        except ValueError:
                print("Invalid Input")
                print("------------------------------------------------------------------------------\n\n\n")
        except EOFError:
                print("Invalid Input")
                print("------------------------------------------------------------------------------\n\n\n")

# CONTINUATION
        print("\n\nType '\033[38;2;255;165;0mEND\033[38;2;212;212;212m' TO EXIT")
        print("Type '\033[38;2;255;165;0mCLS\033[38;2;212;212;212m' to clear screen and continue")
        print("Hit the \033[38;2;255;165;0mENTER KEY\033[38;2;212;212;212m to continue without clearing screen")

        continuationSelector = input("\nEnter your choice: \033[38;2;255;165;0m")
        print("\033[38;2;212;212;212m", end="")



        if continuationSelector.lower() == 'end':
                for i in range (1, 4):
                        print(f"TERMINATING IN \033[38;2;255;165;0m{4 - i}\033[38;2;212;212;212m")
                        timer(1)
                        print("\033[F\033K", end="")
                system('cls')
                break
        elif continuationSelector.lower() == 'cls':
                for i in range (1, 4):
                        print(f"Continuing after clearing terminal in \033[38;2;255;165;0m{4 - i}\033[38;2;212;212;212m")
                        timer(1)
                        print("\033[F\033K", end="")
                
                print("------------------------------------------------------------------------------\n\n\n")
                system('cls')
        elif continuationSelector == '':
                print("\033[F\033K", end="")
                print("Enter your choice: \033[38;2;255;165;0m*BLANK*\033[38;2;212;212;212m")
                print(f"Continuing without clearing the screen")
                print("------------------------------------------------------------------------------\n\n\n")
                timer(3)        
        else:
                for i in range (1, 4):
                        print(f"Invalid input. Terminating in \033[38;2;255;165;0m{4 - i}\033[38;2;212;212;212m")
                        timer(1)
                        print("\033[F\033K", end="")
                system('cls')
                break



