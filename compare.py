def get_number(n):
    while True:
        try:
            return float(input(n))
        except ValueError:
            print("That's not a valid number. Please try again.")

def compare_numbers(a, b):
    if a == b:
        print("They're the same.")
    else:
        print("They're different.")

n1 = get_number("Enter the 1st number: ")
n2 = get_number("Enter the 2nd number: ")

compare_numbers(n1, n2)