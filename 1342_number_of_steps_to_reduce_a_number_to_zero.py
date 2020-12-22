def numberOfSteps(num: int) -> int:
    count = 0
    while num != 0:
        if num % 2 == 0:
            num /= 2
        else:
            num -= 1
        count += 1
    return count
print(numberOfSteps(14))
print(numberOfSteps(8))
print(numberOfSteps(123))