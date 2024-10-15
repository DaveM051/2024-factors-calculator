# Generates headings (eg: ---- Heading ----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instruction", "*")

    print('''

- To use this program please type in an integer in the range between 1 and 200.
The program will show the factors of your chosen integer.

- It will also remind you if your chosen number is...
Unity
A prime number (it only has two factors)
A perfect square (has an odd number of factors)


If you want to exit the program please enter 'xxx'.
    ''')


# Ask user for an integer between 1 and 200.
def num_check(question):
    error = "Please enter a number that is more than zero\n"

    while True:

        try:

            # ask the user for a number
            response = float(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine Goes Here

statement_generator("The Ultimate Factor Finder", "-")

# Display instructions if requested
want_instructions = input("\nPress <enter> to read the instructions "
                          "or any key to continue ")

if want_instructions == "":
    instructions()

while True:
    to_factor = num_check("To factor: ")
    print("You chose to factor", to_factor)

    if to_factor == "xxx":
        break
