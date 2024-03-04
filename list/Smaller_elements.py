"""
Problem -> Return list  of element which is lesser than the threshold element
"""

def get_element(l:list, threshold:int) -> list:
    
    elements = []
    for num in l:
        if num < threshold:
            elements.append(num)
            
    return elements    