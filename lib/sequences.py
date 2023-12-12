#!/usr/bin/env python3

def print_fibonacci(length):
    fib_sequence = [0, 1]
    while len(fib_sequence) < length :
        num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(num)
    print(fib_sequence[:length])

print_fibonacci(9)