# 1. Write a Python program which accepts the radius of a circle from the user and compute the area.
# 2. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
# 3.Write a Python program to display the current date and time.
# Developed by : Yamini Rathod C0796390
# Original Date : 22-05-2021
# Modified Date : 06-06-2021

# Import the modules into main file for the execution
import welcome_qus1
import welcome_qus2
import welcome_qus3
import calculateArea
import calculateAreaTK
import reverseOrder
import reverseOrderTK
import currentDateTime

endOfProgram = 'No'

if __name__ == '__main__':
    while endOfProgram != 'Yes':
        # Defining Menu
        print('-------------------- Menu ----------------------')
        print('1. Run program to find the area of circle using simple method')
        print('2. Run program to find the area of circle using tk interface')
        print('3. Run program to reverse the order of name using simple method')
        print('4. Run program to reverse the order of name using tk interface')
        print('5. Run program to display current date and time')
        print('6. Exit the main program')
        print('------------------------------------------------')

        # Give a choice to user
        choice = input('Please enter your choice : ')
        if choice == '1':
            welcome_qus1.print_welcome()
            calculateArea.calculateAreaOfCircle()
        elif choice == '2':
            welcome_qus1.print_welcome()
            calculateAreaTK.calculateAreaOfCircle()
        elif choice == '3':
            welcome_qus2.print_welcome()
            reverseOrder.reverseOrderName()
        elif choice == '4':
            welcome_qus2.print_welcome()
            reverseOrderTK.reverseOrderName()
        elif choice == '5':
            welcome_qus3.print_welcome()
            currentDateTime.currentDateTimeDisplay()
        elif choice == '6':
            print('Thanks for running the program!')
            exit(0)

        # Check if user wants to continue execution
        endOfProgram = input("\nDo you want to end the program? Press 'Yes' to Exit the program. Press 'No' to run again : ")