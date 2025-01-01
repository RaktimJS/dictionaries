"""
TURN LINE WRAPPING OFF FOR A BETTER VIEW

+-------------------------------------------------------------------+
|***------------   MODULE   ------------***                         |
|                                                                   |
|                                                                   |
|Author: Raktim JS                                                  |
|Institution: Pathsala Public School, Pathsala, Seuj Nagar, 781325  |
|Date: 29/12/2024                                                   |
|Email: raktimunreal4@gmail.com                                     |
|                                                                   |
|                                                                   |
|                        DO NOT PLAGIARISE                          |
|                                                                   |
|                                                                   |
|Includes functions to:                                             |
|        1. Check is a particular key exists in a dictionary        |
|        2. Write all numbers from 1 to n (input) and their squares |
|           as key-value pair                                       |
|        3. Present every character and their number of appearences |
|           as key-value pair for any string                        |
|        4. Update an element in a list that is present as a value  |
|           of a key-value pair in a dictionary                     |
|        5. Fetch the keys of minimum and maximum values from a     |
|           dictionary                                              |
+-------------------------------------------------------------------+

Last Edited on 30/12/2024

"""




# SETUP
import os
from random import randint

os.system('cls')


cmmnNouns = (
        "Apple", "Book", "Car", "Dog", "Flower",
        "House", "Key", "Lamp", "Mountain", "Notebook",
        "Orange", "Pen", "Queen", "River", "Shoe",
        "Table", "Umbrella", "Village", "Window", "Zebra"
)

names = [
        "Alice", "Brian", "Catherine", "David", "Emma",
        "Frank", "Grace", "Henry", "Isabel", "Jack",
        "Katherine", "Liam", "Maria", "Nathan", "Olivia",
        "Peter", "Quinn", "Rachel", "Sophia", "Thomas"
]

intList = []

for i in range(1, 51):
        intList.append(i)

# ABSTRACTS
def randListGenerator(List, ListLen):
        List = List[:]

        i = 0
        newList = list()

        while i < ListLen:
                randomIndex = randint(0, len(List) - 1)
                newList.append(List[randomIndex])

                List.remove(List[randomIndex])

                i += 1        

        return newList

def randDictGenerator(DictKeyList, DictValueList, Length):
        DictKeyList = randListGenerator(DictKeyList, Length)
        DictValueList = randListGenerator(DictValueList, Length)

        newDict = dict()
        i = 0

        while i < len(DictKeyList):
                newDict[DictKeyList[i]] = DictValueList[i]
                i += 1

        return newDict

def _textWritter(j):
        if j == 1:
                text = "MATH"
        elif j == 2:
                text = "PHYSICS"
        else:
                text = "CHEMISTRY"
        
        return text




# Key searcher (Gamified)
def isKeyAvailable():
        print("\n\n\n\033[4m\033[38;2;255;255;255mFIND ANY KEY IN THE HIDDEN DICTIONARY FROM THE GIVEN POSSIBLE KEYS\033[38;2;212;212;212m\033[0m\n\n")
        print("Possible keys: \n")

        for i in names:
                print(f"{i}", end="")

                if names.index(i) != len(names) - 1:
                        print(", ", end = "")

                if (names.index(i) + 1)  % 5 == 0:
                        print()

        dictionary = randDictGenerator(names, intList, 8)

        i = 1

        while i <= 3:
                print(f"\n\nChance {i}")

                keyInput = input("\nGuess a key from the hidden dictionary: \033[38;2;0;0;255m")
                print("\033[38;2;212;212;212m", end="")

                if keyInput.capitalize() in dictionary:
                        print(f"Yes! {keyInput.capitalize()} is present as a key in the dictionary!")
                        break
                else:
                        print(f"No! {keyInput.capitalize()} is not in dictionary! Try again.")

                i += 1

        print("\n\nThe dictionary was: \n")

        for i in dictionary:
                print(f"\033[38;2;255;255;255m{i}\033[38;2;212;212;212m  \033[38;2;255;0;0m:\033[38;2;212;212;212m  \033[38;2;255;255;255m{dictionary[i]}\033[38;2;212;212;212m")


# Square maker
def squares():
        print("\033[4m\033[38;2;255;255;255m\n\n\nSQUARES OF ALL INTEGERS FROM 1 to ANY NUMBER\033[38;2;212;212;212m\033[0m\n")

        while True:
                intInput = input("\nEnter a number: \033[38;2;255;165;0m")
                print("\033[38;2;212;212;212;212m", end="")

                try:
                        intInput = int(intInput)

                        if intInput > 1 and type(intInput) == int:
                                numToSquare = dict()
                                i = 1

                                while i <= intInput:
                                        numToSquare[i] = i*i
                                        i += 1

                                print(f"The dictionary of squares from 1 to {intInput} is: \n")
                                        
                                for i in numToSquare:
                                        print(f"{i} \033[38;2;255;0;0m:\033[38;2;212;212;212m {numToSquare[i]}")

                                break
                        elif intInput == 1 and type(intInput) == int:
                                print("The square of 1 is 1")
                                
                                break
                        else:
                                print("Value can't be smaller than 1")
                except ValueError:
                        print("Invalid Input. Enter a integral value")
                except EOFError:
                        print("Invalid Input. Enter a integral value")


# Character counter
def charCounter():
        print("\033[4m\033[38;2;255;255;255m\n\n\nCOUNT ALL CHARACTERS IN ANY TEXT\033[38;2;212;212;212m\033[0m\n\n")
        string = input("Enter a string: \033[38;2;255;165;0m")
        print("\033[38;2;212;212;212;212m", end="")

        string = string.upper()

        if string != '':
                countedDict = dict()
                strList = list()

                for i in string:
                        strList.append(i)

                for i in strList:
                        count = strList.count(i)
                        countedDict[i] = count

                        while count == 0:
                                strList.remove[i]
                                count -= 1

                print(f"The dictionary of the character and their counts in \033[38;2;255;165;0m{string}\033[38;2;212;212;212m is: \n")

                for i in countedDict:
                        print(f"No. of appearences of {i}  :  {countedDict[i]}")
        else:
                print("The entry is blank")


# Update elemnt in a list, present as a value
def updateElement():
        print("\033[4m\033[38;2;255;255;255m\n\n\nUPDATES LISTS PRESENT AS VALUES IN A DICTIONARY\033[38;2;212;212;212m\033[0m\n\n")
        print("Format:\n        [SUBJECT NAME: TEST 1, TEST 2, TEST 3]\n")

        print("\n\033[38;2;200;0;0m→ Leave the field \033[38;2;255;165;0mBLANK\033[38;2;200;0;0m and \033[38;2;255;165;0mHIT ENTER\033[38;2;200;0;0m to move to next field without any change")
        print("→ ANY UNSUPPORTED VALUES WILL DIRECTLY TERMINATE THE PROGRAM")
        print("→ SUPPORTS ONLY INTEGERS\033[38;2;212;212;212m\n\n")

        pcmDict = {
                'Math': [88, 89, 90],
                'Physics': [92, 94, 89],
                'Chemistry': [90, 87, 93]
        }

        print()

        for i in pcmDict:
                print(f"{i} : {pcmDict[i]}")

        i = 1
        j = 1

        while j <= 3:
                print(f"\n{_textWritter(j)}")

                while i <= 3:
                        print(f"\033[38;2;212;212;212mTest {i}: \033[38;2;255;165;0m", end="")
                        marks = input()
                        print("\033[38;2;212;212;212m", end="")

                        try:
                                if marks != '':
                                        marks = int(marks)
                                        pcmDict[f"{_textWritter(j).capitalize()}"][i-1] = marks
                                        i += 1
                                elif marks == '':
                                        print(f"\033[A\033[KTest {i}: \033[38;2;255;165;0m*BLANK*\033[32;2;212;212;212m")
                                        i += 1
                        except ValueError:
                                print("Invalid Input 3. Terminating")
                                j = 4
                                i = 4
                        except EOFError:
                                print("Invalid Input 4. Terminating")
                                j = 4
                                i = 4
                                
                
                i = 1
                j += 1

        print()

        for i in pcmDict:
                print(f"{i} : {pcmDict[i]}")


# Min-Max fetcher
def minMaxFetcher():
        list1 = names[:]
        list1.extend(cmmnNouns)
        dict1 = randDictGenerator(list1, intList, 5)
        keyList = list()
        valueList = list()

        print(f"Random dict: \n")

        for i in dict1:
                print(f"{i}  \033[38;2;200;0;0m:\033[38;2;212;212;212m  {dict1[i]}")

        print("\n")

        keyList.extend(dict1.keys())
        valueList.extend(dict1.values())

        minMaxDict = {
                "MAXIMUM: \n        " + keyList[valueList.index(max(valueList))] : max(valueList),
                "MINIMUM: \n        " + keyList[valueList.index(min(valueList))] : min(valueList)
        }

        for i in minMaxDict:
                print(f"{i}  \033[38;2;200;0;0m:\033[38;2;212;212;212m  {minMaxDict[i]}\n")

        print()



