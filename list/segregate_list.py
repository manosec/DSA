"""
Problem searete the list into two different categories
"""

def segregate(l: list) -> list:
    odd = []
    even = []
    for num in l:
        if num % 2 ==0:
            even.append(num)
        else: odd.append(num)
        
    return odd, even