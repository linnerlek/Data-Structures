# Linn Erle Klofta
# CSC 2720 Lab #1
# Lab time: Friday 1-1:50pm
# Due time: 01/14/2024 @ 11:59pm

# Program description: This program will ask the user to think of a number between 0 and n-1, where n is a positive integer

def guess_my_number():
    n = int(input("Enter n: "))
    while n <= 0:
        # makes sure the user inputs a positive value for n
        n = int(input("Enter a positive integer for n: "))

    print("Welcome to Guess My Number!")
    print(f"Please think of a number between 0 and {n-1}.")

    low = 0
    high = n
    guess = (low + high) // 2

    while True:
        print(f"Is your number: {guess}?")
        response = input(
            "Please enter C for correct, H for too high, or L for too low.\nEnter your response (H/L/C): ")

        if response == "C":
            print("Thank you for playing Guess My Number!")
            break
        elif response == "H":
            high = guess + 1
        elif response == "L":
            low = guess

        guess = (low + high) // 2


guess_my_number()