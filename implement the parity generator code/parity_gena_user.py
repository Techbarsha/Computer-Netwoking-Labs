def generate_even_parity(binary_pattern):
    # Check if the input is a valid binary string
    if not all(bit in '01' for bit in binary_pattern):
        raise ValueError("Input should be a binary string")

    # Count the number of 1s in the binary pattern
    count_of_ones = binary_pattern.count('1')
    
    # Determine the parity bit (0 if the count of 1s is even, 1 if odd)
    if count_of_ones % 2 == 0:
        parity_bit = '0'
    else:
        parity_bit = '1'
    
    # Append the parity bit to the original pattern
    parity_pattern = binary_pattern + parity_bit
    
    return parity_pattern

# Get binary pattern from user input
binary_pattern = input("Enter a binary pattern: ")

try:
    parity_pattern = generate_even_parity(binary_pattern)
    print(f"Original pattern: {binary_pattern}")
    print(f"Pattern with even parity bit: {parity_pattern}")
except ValueError as e:
    print(e)
