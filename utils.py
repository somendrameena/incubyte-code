def add(numbers: str = "") -> int:

    if numbers == "":
        return 0
    
    int_nums = [int(num) for num in numbers.split(",")]

    negative_nums = [num for num in int_nums if num < 0]
    if len(negative_nums) > 0:
        raise Exception("negative numbers not allowed")

    count = 0

    for num in int_nums:
        count += num

    return count
