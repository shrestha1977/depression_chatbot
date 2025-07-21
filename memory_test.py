# memory_test.py
import random

def generate_sequence(length=5):
    return [random.randint(1, 9) for _ in range(length)]

def check_sequence(user_input, actual_sequence):
    try:
        user_sequence = list(map(int, user_input.strip().split()))
        return user_sequence == actual_sequence
    except:
        return False
