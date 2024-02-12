def most_occurred_number(lst):
    if not lst:
        return None

    # Using a dictionary to count occurrences of each element
    count_dict = {}
    max_occurrences = 0
    most_occurred_element = None

    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

        # Update the most occurred element if needed
        if count_dict[num] > max_occurrences:
            max_occurrences = count_dict[num]
            most_occurred_element = num
    return most_occurred_element

# Example usage:
my_list = [1, 2, 3, 5, 4, 2, 2, 3, 3, 3, 5, 5, 5, 5, 3,3,3]
result = most_occurred_number(my_list)
print(f"The most occurred number is: {result}")
