def average(l: list) -> int:
    """_summary_

    Args:
        l (list): _description_

    Returns:
        int: can also use this as return sum(l)/len(l)
    """
    sum = 0 
    for num in l:
        sum += num
    length = len(l)
    return sum/length

