def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    if not numbers:
        return None  
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
    max_num = numbers[0]
    # If a larger number is found, compare and update max_num
    # Return the largest number
    print("max_num")


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
