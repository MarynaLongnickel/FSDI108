
# 1 - Sum
def add(a, b):
    return a + b

# 2 - Subtract
def subtract(a, b):
    return a - b

# 3 - Multiplication
def multiply(a, b):
    return a * b

# 4 - Division
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# 5 - Guess my age
def guess_my_age():
    secret_age = 25  # Set your desired age here
    while True:
        try:
            guess = int(input("Guess my age: "))
            if guess == secret_age:
                print("Correct! You guessed my age.")
                break
            elif guess < secret_age:
                print("Too low, try again.")
            else:
                print("Too high, try again.")
        except ValueError:
            print("Please enter a valid number.")

# Demo
if __name__ == "__main__":
    a = 10
    b = 5

    print(f"Sum: {a} + {b} = {add(a, b)}")
    print(f"Subtract: {a} - {b} = {subtract(a, b)}")
    print(f"Multiply: {a} * {b} = {multiply(a, b)}")
    print(f"Divide: {a} / {b} = {divide(a, b)}")

    # Run the guessing game
    guess_my_age()
