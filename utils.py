def add(numbers: str = "") -> int:

    # Return zero if string is blank
    if numbers == "":
        return 0

    # Set default delimiter
    delimiter = ","

    # Replace \\n (if received) with new line character
    numbers = numbers.replace("\\n", "\n")
    
    # Find delimiter from string
    if numbers.startswith("//"):
        delimiter = numbers[2]
        numbers = numbers[4:]
    
    # Replace new line character with delimiter
    numbers = numbers.replace("\n", delimiter)
    
    # Create list of numbers from string
    int_nums = [int(num) for num in numbers.split(delimiter)]

    # Check for negative numbers
    negative_nums = [num for num in int_nums if num < 0]
    if len(negative_nums) > 0:
        error_nums = ",".join(map(str, negative_nums))
        raise Exception("negative numbers not allowed {}".format(error_nums))

    # Add numbers to calculate sum
    sum = 0
    for num in int_nums:
        sum += num

    # Return value of sum
    return sum
