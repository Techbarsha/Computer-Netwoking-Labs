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

# Get user input for start, end, and step
try:
    start = int(input("Enter the start value: "))
    end = int(input("Enter the end value (non-inclusive): "))
    step = int(input("Enter the step size: "))
    
    # Example usage
    print("Generated sequence:")
    for number in counter_generator(start, end, step):
        print(number)
except ValueError:
    print("Please enter valid integer values for start, end, and step.")
