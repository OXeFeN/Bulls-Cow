#   HW-PY-7-Novak
#   Develop a game of Bulls and Cows. The program chooses a four-digit number, and the player has to guess it.
#   After the user enters a number, the program reports how many digits of the number are guessed (bulls),
#   and how many digits are guessed and stand in the right place (cows). After guessing the number,
#   print the number of user's attempts. Use recursion in your game.

import random
from random import randint, shuffle
import json


file_path = "High-score.txt"

def initialize():
    return [], [], []

def god_top_rnd(digits):
    tl = ""
    for i in range(digits):
        tl = tl + "9"
    return int(tl)

def try_function(tries, sec):
    global imp
    if tries == 0:
        imp = str(input(f"Secret number has {len(sec)} digits. Guess now!"))
        validate_input(sec)
        print(f"Your guess: {imp}")
        tries += 1
    else:
        imp = str(input("Try again! "))
        validate_input(sec)
        print(f"Your guess: {imp}")
    return imp

def win(tries):
    if tries == 1:
        print(f"You are absolute God! You need just {tries} try!")
    else:
        print(f"Awesome! You need just {tries} tries!")

def validate_secret(sec, top):
    result = len(top) - len(sec)
    prefix = ""
    for i in range(result):
        prefix = prefix + "0"
    sec = prefix + sec
    return sec

def false_check(che, imp):
    for num in imp:
          che.append(False)
    return che

def validate_input(sec):
    while True:
        global imp
        if validate_input_len(sec) and validate_input_num():
            return imp

def validate_input_num():
    global imp
    if imp.isnumeric():
        return True
    else:
        print("secret is only numbers.")
        imp = input("Please, enter only numbers: ")
        return False

def validate_input_len(sec):
    global imp
    if len(imp) == len(sec):
        return True
    else:
        print(f"Error: Incorrect number of digits. Secret number is {len(sec)} digits long.")
        imp = input("Please insert new guess: ")
        return False

def guess_bulls(imp, sec, bulls, checked):
    for index, num in enumerate(imp):
        if num == sec[index]:
            bulls.append(num)
            checked[index] = True
        else:
            checked[index] = False
    random.shuffle(bulls)
    return bulls

def guess_cow(imp, sec, cows):
    for index, num in enumerate(sec):
        if num in imp:
            cows.append(num)
    random.shuffle(cows) #Milion dollar question: Why i need to shuffle those numbers?
    return cows

def remover(sec, che):
    secret2 = []
    for index, bool in enumerate(che):
        if bool == False:
           secret2.append(sec[index])
    return secret2

def guess(sec):
    tries = 0
    player = str(input("Insert player name: ").strip())
    while True:
        imp = try_function(tries, sec)
        if str(imp) == str(sec):
            tries += 1
            win(tries)
            break
        else:
            tries += 1
            bulls, cows, checked = initialize()
            checked = false_check(checked, imp)
            bulls = guess_bulls(imp, sec, bulls, checked)
            cows = guess_cow(imp, remover(sec, checked), cows)
            hint_bulls(bulls)
            hint_cows(cows)
    return tries, player

def hint_bulls(bulls):
    if not bulls:
        print("Bad luck! No number was correct.")
    else:
        bulls = " ".join(str(num) for num in bulls)
        print(f"Numbers {bulls} are correct and on the right position.")
    return bulls

def hint_cows(cows):
    if not cows:
        print("No other correct numbers.")
    else:
        cows = " ".join(str(num) for num in cows)
        print(f"numbers {cows}  are correct but on the wrong position")
    return cows
    
def print_bad_input():
    print("Bad input, follow the main menu instructions")

def main_menu():
    print("""
            ---------- MAIN MENU ----------
            [1] -> 4 DIGITS MODE
            [2] -> GOD MODE
            [3] -> PRINT LEADER BOARD

            [0] -> EXIT
            """)
    
#file functions
def file_update(file_path, player, tries):
    try:
        with open(file_path, "a") as file:
            file.write(f"{player}: {tries}\n")
            return True
    except OSError as error:
        print("Something goes wrong!", error)
        return False
    
def file_load(file_path):
    try:
        with open(file_path, "r") as file:
            output = file.readlines(file)
        return output
    except OSError as error:
        print("Something goes wrong!", error)
        return None

def BullsCows():
    while True:
        try:
            main_menu()
            user_choice = int(input("Choose from main menu: "))
        
            if user_choice == 1:
                print("Chosen mode: 4 DIGITS MODE")
                noob_secret = validate_secret(str(randint(0,9999)), "9999")
                tries = guess(noob_secret)
                file_update(file_path, player, tries)

            elif user_choice == 2:
                print("You choose a GOD MODE! Guessed number can be any number!")
                top_limit = god_top_rnd(int(input("Insert how many digits you can beat: ")))
                god_secret = validate_secret(str(randint(0,top_limit)), str(top_limit))
                guess(god_secret)
            elif user_choice == 3:
                player = input("Insert player name: ").strip()
            elif user_choice == 4:
                print("WIP " * 5)

            elif user_choice == 0:
                print("Program shutdown.")
                break
            else:
                print_bad_input()
                main_menu()
        except:
            user_choice = 7
            print_bad_input()

if __name__ == "__main__":
    BullsCows()