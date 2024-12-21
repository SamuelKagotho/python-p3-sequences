#!/usr/bin/env python3

def print_fibonacci(length):

    if length <= 0:
        print([])
        return

    fibonacci_sequence = [0, 1]

    for _ in range(2, length):
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)

    print(fibonacci_sequence[:length])

print_fibonacci(9)
