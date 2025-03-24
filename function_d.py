def max_value(numbers):
    value = 0
    for number in numbers:
        value +=1
    return value

if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
