import random


size = int(input("Enter list size: "))

def create_list(size):
    numbers = [[random.randint(100,999) for j in range(size)] for i in range(size)]
    return numbers 