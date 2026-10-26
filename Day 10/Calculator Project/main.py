from art import logo
print(logo)


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return  n1 * n2

def divide(n1, n2):
    return n1 / n2

Operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


calculate_over= False
while not calculate_over:

    first_number =int(input("What is your first number?"))
    for symbol in Operations:
        print(symbol)
    which_operation = input("What's your operation? " )

    next_number = int(input("What's your next number"))

    result = Operations[which_operation](first_number, next_number)
    print(f"{first_number} {which_operation} {next_number} = {result}")

    last_question = input(f"type 'y' to continue with {result}, or type 'n' to start a new calculation"
      f" ")

    continue_calculation = True
    while continue_calculation:
        if last_question == "y":
            for symbol in Operations:
                print(symbol)
            which_operation = input("What's your operation? ")
            next_number = int(input("What's your next number"))
            result_2 = Operations[which_operation](result, next_number)
            print(f"{result} {which_operation} {next_number} = {result_2}")

            last_question = input(f"type 'y' to continue with {result_2}, or type 'n' to start a new calculation"
                                      f" ")
            if last_question == "y":
                result = result_2
            else:
                continue_calculation = False
                print("\n " * 20 )
        else:
            continue_calculation = False


