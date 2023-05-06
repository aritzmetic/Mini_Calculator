# Delera, Aritz B.

import operator
import random
import time
import pyfiglet

opening = pyfiglet.figlet_format("= O.O.P =", font="starwars")
print(opening)

# Create an introduction
print("=" * 61)
print(" Welcome to AritzMetic's Calculator! ".center(60, "+"))
print("=" * 61)

# Ask the name of the user to create a greeting
name = input("\033[30mHi Smart Pipol! what is your name?: \033[0m")
print()
print("\033[40mHi", name, "! AritzMetic is here to help you in solcing your Maths!\033[0m")

# Define the calculator method
def calculator():
    print()

# use while loop and try method for calculations
while True:
    try:
        # display the operations that the user can use
        trivia = [
            "Did you know that the word 'addition' comes from the Latin word 'addere', which means 'to give more'?", 
            "Did you know that the word 'subtraction' comes from the Latin word 'subtrahere', which means 'to take away'?", 
            "Did you know that the word 'multiplication' comes from the Latin word 'multiplicare', which means 'to increase in number'?",
            "Did you know that the word 'division' comes from the Latin word 'dividere', which means 'to separate'?"
        ]

        time.sleep(2)
        print()
        print("+" * 61)
        print()
        print("\033[30mPress the Letter of operation your choice!\033[0m")
        print()
        print("-" * 61)
        print()
        print("A for Addition".center(60))
        print("S for Subtraction".center(60))
        print("M for Multiplication".center(60))
        print("D for Division".center(60))
        print()
        print("-" * 61)
        print()
        print(random.choice(trivia))
        print()
        print("+" * 61)
        time.sleep(2)


        # create dictionary of the correponding function of the operation
        operator_dictionary = {"A": operator.add, "S": operator.sub, "M": operator.mul, "D": operator.truediv}
        # ask the user for the operator they want to use
        print()
        user_operation = input("\033[31mWhich of the available operators would you like to make use of?: \033[0m")

        # check the validity of the operator by using if-else statement
        if user_operation in operator_dictionary:
            # if valid, ask the user for first and second numbers
            number_1 = float(input("\033[32mType in the first number of what you wish to calculate: \033[0m"))
            number_2 = float(input("\033[32mType in the second number of what you wish to calculate: \033[0m"))
            # Calculate and dispaly the result
            result = operator_dictionary[user_operation](number_1, number_2)
            time.sleep(2)
            print()
            print(":" * 61)
            print("\033[33mProcessing...\033[0m" .center(60))
            print(":" * 61)
            print()
            time.sleep(2)
            print(f"\033[41mWe appreciate your willingness to wait. The result of your math is {result}!\033[0m")
        # else, Ask for the user's input, and keep going until they provide something that works.
        else:
            print("\033[30mThere is a problem with the operator you entered, possibly due to incorrect capitalisation or invalid operation. Could you just give it another shot?\033[0m")
            continue

        # ask the user if they want to repeat the process
        time.sleep(2)
        print()
        print("<>" * 61)
        print()
        question = input("\033[36mDo you wish to make another Calculations? (Y/N): \033[0m")
        # break the loop if they wish to stop the program
        if question.upper() == "N":
            goodbye_quotes = ["Mathematics is the language in which God has written the universe. - Galileo Galilei","In mathematics, the art of proposing a question must be held of higher value than solving it. - Georg Cantor","The study of mathematics, like the Nile, begins in minuteness but ends in magnificence. - Charles Caleb Colton"]
            print("Thank you for using AritzMetic's Calculator!\n{}".format(random.choice(goodbye_quotes)))
            closing = pyfiglet.figlet_format(" = THE END = ", font="doom")
            print(closing)
            break
        # raise ValueError if they inputted incorrect value
        elif question.upper() != "Y":
            raise ValueError("\033[30mThe option you selected is not valid. Please enter 'Y' or 'N'.\033[0m")
    # Manage runtime exceptions that could arise.
    except ValueError:
        print("\033[30mInvalid Value. Please input another value.\033[0m")
    except ZeroDivisionError:
        print("\033[30mInvalid Divisor. Zero is not applicable in as a divisor!\033[0m")
    except TypeError:
        print("\033[30mInvalid data. Please try again\033[0m")
