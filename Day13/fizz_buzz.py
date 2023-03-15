for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:  # change if-statement from "or" to "and"
        print("FizzBuzz")
    elif number % 3 == 0:  # change "if" into "elif"
        print("Fizz")
    elif number % 5 == 0:  # change "if" into "elif"
        print("Buzz")
    else:
        print(number)  # change array of number into just number
