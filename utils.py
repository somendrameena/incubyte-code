def add(numbers: str = "") -> int:

    if numbers == "":
        return 0
    
    splitted_str = numbers.strip().split(",")

    count = 0

    for num in splitted_str:
        num_int = int(num)
        if num_int < 0:
            raise Exception("negative numbers not allowed")

        count += num_int

    return count
