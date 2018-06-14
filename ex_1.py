import random

def create_list(value):
    numbers = []
    for i in range(value):
        numbers.append([])
        for j in range(value):
            numbers[i].append(random.randint(100, 999))
    return numbers
