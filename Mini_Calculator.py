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
    try:
        # display the operations that the user can use
        print("Type the name of the operation your choice!")
        print("ADD for Addition")
        print("SUBTRACT for Subtraction")
        print("MULTIPLY for Multiplication")
        print("DIVIDE for Division")
        
# create dictionary of the correponding function of the operation
# ask the user for the operator they want to use
# check the validity of the operator by using if-else statement
# if valid, ask the user for first and second numbers
# Calculate and dispaly the result
# else, Ask for the user's input, and keep going until they provide something that works.

# ask the user if they want to repeat the process
# break the loop if they wish to stop the program
# raise ValueError if they inputted incorrect value
# Manage runtime exceptions that could arise.
