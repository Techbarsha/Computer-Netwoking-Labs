def counter_generator(start, end, step=1):
    """
    A generator function that generates a sequence of numbers from start to end with a specified step.
    
    :param start: The starting value of the sequence.
    :param end: The ending value of the sequence (non-inclusive).
    :param step: The step size between values in the sequence.
    """
    current = start
    while current < end:
        yield current
        current += step

# Example usage
for number in counter_generator(0, 10, 2):
    print(number)
