#   HW-PY-7-Novak
#   Develop a game of Bulls and Cows. The program chooses a four-digit number, and the player has to guess it.
#   After the user enters a number, the program reports how many digits of the number are guessed (bulls),
#   and how many digits are guessed and stand in the right place (cows). After guessing the number,
#   print the number of user's attempts. Use recursion in your game.

from random import randint

user_fguest = int(input("Isert your guess: "))

def top_rnd(imp):
    tl = ""
    for i in range(len(str(imp))):
        tl = tl + "9"
    return int(tl)
top_limit = top_rnd(user_fguest)
seceret = randint(0,top_limit)
print(numbers)

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

def BullsCows():
    while True:
        try:
            main_menu()
            user_choise = int(input("Choose from main menu: "))
        
            if user_choise == 1:
                main_menu()
                employees.append(add_employee())
                file_update(employees)

            elif user_choise == 2:
                fire_menu()
                user_choise2 = int(input("Choose from fire menu: "))
                if user_choise2 == 1:
                    fired_employees.append(del_employee(employees))
                    user_choise3 = str(input("Do you want you want print a list of fired employees? (Y / N) : "))
                    if user_choise3.strip().lower() == "y":
                        print_a_list(fired_employees)
                if user_choise2 == 2:
                    print_a_list(fired_employees)

            elif user_choise == 3:
                #search_menu()
                #search(employees)
                print_a_list(search_employee(employees))
                
            elif user_choise == 4:
                replace_employee(employees)

            elif user_choise == 5:
                print_a_list(employees)
            
            elif user_choise == 6:
                if file_update(employees):
                    print("Update sucessfull!")
                else:
                    print("Try again")

            elif user_choise == 0:
                print("Programe shutdown.")
                break

            else:
                print_bad_input()
                main_menu()
        except:
            user_choise = 7
            print_bad_input()

BullsCows()