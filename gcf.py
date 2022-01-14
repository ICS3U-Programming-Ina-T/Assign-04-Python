#!/usr/bin/env python3

# Created by: Ina Tolo
# Created on: Jan. 7, 2022
# This program determines the GCF
# of two numbers using a 'for' loop.

# declaring variables
num1_int = 0
num2_int = 0
counter = 0


# calculates the LCM of the users numbers
def choiceTwo():
    # input from the user
    num1_string = input("Enter the first whole number: ")
    num2_string = input("Enter the second whole number: ")
    print("")

    try:
        # converts user input to integer
        num1_int = int(num1_string)
        num2_int = int(num2_string)

        # checking if user input is in the correct range
        if num1_int and num2_int >= 0:
            if num1_int > num2_int:
                greater = num1_int
            else:
                greater = num2_int

            # determines LCM
            while(True):
                if ((greater % num1_int == 0) and (greater % num2_int == 0)):
                    lcm = greater
                    greater += 1
                    print("The LCM of {} and {} is {}."
                          .format(num1_int, num2_int, lcm))
                    print("Thanks for playing!")
                    break
        else:
            print("Please enter whole numbers!")
    except Exception:
        print("These are invalid values!")


# function to determine another GCF
def choiceOne():
    # input from the user
    num1_string = input("Enter the first whole number: ")
    num2_string = input("Enter the second whole number: ")
    print("")

    try:
        # converts user input to integer
        num1_int = int(num1_string)
        num2_int = int(num2_string)

        # checking if user input is in the correct range
        if num1_int and num2_int >= 0:
            for counter in range(num1_int, 0, -1):
                if num1_int % counter == 0 and num2_int % counter == 0:
                    print("The GCF of {} and {} is {}."
                          .format(num1_int, num2_int, counter))
                    print("Thanks for playing!")
                    break
        else:
            print("Please enter whole numbers!")
    except Exception:
        print("These are invalid values!")


# determines what the user wants to do next
def newNums():

    # declaring variables
    option1 = "1"
    option2 = "2"
    option3 = "3"

    # getting input from user
    answer = input("Do you want to find the GCF of other numbers (1),"
                   "the LCM of other numbers (2), or neither (3)?: ")
    print("")

    if answer == option1:
        choiceOne()
    elif answer == option2:
        choiceTwo()
    elif answer == option3:
        print("Thanks for playing!")
    else:
        print("Please type a valid response!")
        print("")
        newNums()


# function to determine the GCF
def main():
    # display opening message
    print("Today we will calculate the GCF of two whole numbers!")
    print("")

    # input from the user
    num1_string = input("Enter the first whole number: ")
    num2_string = input("Enter the second whole number: ")
    print("")

    try:
        # converts user input to integer
        num1_int = int(num1_string)
        num2_int = int(num2_string)

        # checking if user input is in the correct range
        if num1_int and num2_int >= 0:
            for counter in range(num1_int, 0, -1):
                if num1_int % counter == 0 and num2_int % counter == 0:
                    print("The GCF of {} and {} is {}."
                          .format(num1_int, num2_int, counter))
                    print("")
                    newNums()
                    break
        else:
            print("Please enter whole numbers!")
    except Exception:
        print("These are invalid values!")


if __name__ == "__main__":
    main()
