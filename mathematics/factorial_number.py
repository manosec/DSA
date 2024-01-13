while True:
    try:
        digit = int(input("Enter digit to calculate the factorial: "))
        break  # Break out of the loop if the input is successfully converted to an integer
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

while True:
    method = input("Choose factorial method (1 for iterative, 2 for recursive): ")
    if method in ('1', '2'):
        method = int(method)
        break
    else:
        print("Invalid input. Please enter 1 or 2.")

def factorial(value):
    calc_value = 1
    for number in range(2, value + 1):
        calc_value = calc_value * number
    return calc_value

def recursive_factorial(value):
    if value == 0: 
        return 1
    return value * recursive_factorial(value-1)

if __name__ == "__main__":
    if method == 1:
        response = factorial(digit)
    elif method == 2:
        response = recursive_factorial(digit)

    print(f"Factorial of a given number {digit} is {response}")
