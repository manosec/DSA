"""Probelm:
Aa person saving 1 rupee on day1, 2 rupee on day2, 3 rupee on day3. Find out total rupee 
saved by the person on day 756
"""
while True:
    try:
        days = int(input('Enter the number of days: '))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

def sum_of_n(n):
    return n*(n+1)/2

if __name__ == "__main__":
    total_rupee = sum_of_n(days)
    print(f"Total Rupee saved by the person is {total_rupee} for {days} days")
        