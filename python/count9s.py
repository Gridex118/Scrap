def count_9s(power_index: int) -> int:
    nine_count = 0
    LOW = 10**(power_index - 1)
    HIGH = 10**power_index - 1
    working_number = LOW
    while working_number <= HIGH:
        for i in str(working_number):
            if i == '9': nine_count += 1
        working_number += 1
    return nine_count


for power_index in range(1,8):
    print(f"{power_index}: {count_9s(power_index)}")
