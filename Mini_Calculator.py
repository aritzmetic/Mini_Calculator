# Delera, Aritz B.

# Create a Simple App Calculator
# 1. The application will ask the user to choose one of the four math operations (Addition, Subtraction, Multiplication and Division)
# 2. The application will ask the user for two numbers
# 3. Display the result
# 4. The application will ask if the user wants to try again or not.
# 5. If yes, repeat Step 1.
# 6. If no, Display “Thank you!” and the program will exit 
# 7. Use Python Function and appropriate Exceptions to capture errors during runtime.

# Import operator module
import operator

# Define the calculator method
def calculator():
    print("Hi!")

# use while loop and try method for calculations
while True:
        # display the operations that the user can use
        print("Press the Letter of operation your choice!")
        print("A for Addition")
        print("S for Subtraction")
        print("M for Multiplication")
        print("D for Division")

        # create dictionary of the correponding function of the operation
        operator_dictionary = {"A": operator.add, "S": operator.sub, "M": operator.mul, "D": operator.truediv}
        # ask the user for the operator they want to use
        user_operation = input("Which of the available operators would you like to make use of?: ")

        # check the validity of the operator by using if-else statement
        if user_operation in operator_dictionary:
            # if valid, ask the user for first and second numbers
            number_1 = float(input("Type in the first number of what you wish to calculate: "))
            number_2 = float(input("Type in the second number of what you wish to calculate: "))
            # Calculate and dispaly the result
            result = operator_dictionary[user_operation](number_1, number_2)
            print(f"We appreciate your willingness to wait. The result of your math is {result}!")
        # else, Ask for the user's input, and keep going until they provide something that works.
        else:
            print("There is a problem with the operator you entered, possibly due to incorrect capitalisation or invalid operation. Could you just give it another shot?")

# ask the user if they want to repeat the process
# break the loop if they wish to stop the program
# raise ValueError if they inputted incorrect value
# Manage runtime exceptions that could arise.
