while True:
    try:
        digit = int(input("Enter digit to check for palindrome: "))
        break  # Break out of the loop if the input is successfully converted to an integer
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


def check_palindrome(digit):
    rev = 0
    comparison_value = digit
    while digit != 0:
        #Simple math hack to get the last value in the given digit
        last_digit = digit % 10
        #Multiplying by 10 and adding the last_digit to compare the reversed values 
        rev = rev * 10 +  last_digit
        #To pop the last value from the given digit
        digit = digit // 10

    if rev == comparison_value:
        return "It is a palindrome!"
    return "It is not a palindrome :("


if __name__ == "__main__":
    response = check_palindrome(digit)
    print(response)