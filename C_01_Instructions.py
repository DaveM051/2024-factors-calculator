# Generates headings (eg: ---- Heading ----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instruction", "*")

    print('''

- To use this program please type in an integer in the range between 1 and 200.
The program will show the factors of your chosen integer.

- It will also remind you if your chosen number...
is a price number (ie: ir has two factors)
is a perfect square

If you want to exit the program please enter 'xxx'.
    ''')


# Main routine goes here

# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue ")

if want_instructions == "":
    instructions()

print("program continues")
