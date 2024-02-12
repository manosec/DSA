"""Probelm:
Given the two number return the greatest common divisor.
"""

        
def gcd_euclidean(a, b):
    while a != b:
        if a < b:
            b = b - a
        else:
            a = a - b
    return a 

def gcd_euclidean_recursive(a, b):
    if b==0:
        return a
    return gcd_euclidean_recursive(b, a%b)


if __name__ == "__main__":
    a = int(input("Enter the first number (a): "))
    b = int(input("Enter the second number (b): "))

    while True:
        print("Choose GCD calculation method:")
        print("1. Euclidean Algorithm (Iterative)")
        print("2. Euclidean Algorithm (Recursive)")

        choice = int(input("Enter your choice (1 or 2): "))

        if choice == 1:
            gcd_value = gcd_euclidean(a, b)
            break
        elif choice == 2:
            gcd_value = gcd_euclidean_recursive(a, b)
            break
        else:
            print("Invalid choice. Please enter 1 or 2. Try again.")

    print(f"The Greatest Common Divisor of both {a} and {b} is {gcd_value}")