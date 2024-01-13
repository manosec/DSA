while True:
    try:
        digit = int(input("Enter the digit to count the length: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

def count_digits(value):
    steps = 0
    while value > 0:
        #Floor division to receive whole number and to remove last digit in the given digit
        value = value//10
        steps +=1 
    return steps

if __name__ == "__main__":
    length_of_digit = count_digits(digit)
    print(f"The length of the given digit {digit} is {length_of_digit}")
    