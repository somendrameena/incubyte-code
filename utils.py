def add(numbers: str = "") -> int:

    if numbers == "":
        return 0

    delimiter = ","
    
    if numbers.startswith("//"):
        delimiter = numbers[2]
        numbers = numbers[4:]
    
    numbers = numbers.replace("\n", delimiter)
    
    int_nums = [int(num) for num in numbers.split(delimiter)]

    negative_nums = [num for num in int_nums if num < 0]
    if len(negative_nums) > 0:
        error_nums = ",".join(map(str, negative_nums))
        raise Exception("negative numbers not allowed {}".format(error_nums))

    sum = 0

    for num in int_nums:
        sum += num

    return sum
