def add(numbers: str = "") -> int:
    
    splitted_str = numbers.strip().split(",")

    count = 0

    for num in splitted_str:
        num_int = int(num)
        count += num_int

    return count
