# Ask the user for width and loop until they
# enter a number that is more than zero
def num_check(question):
    error = "Please enter a number that is between 1 and 200 inclusive\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            # ask the user for a number
            response = int(response)

            # check that the number is more than zero
            if 1 <= response <= 200:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine Goes Here
while True:
    to_factor = num_check("To factors: ")
    print("You chose to factor", to_factor)

    if to_factor == "xxx":
        break
