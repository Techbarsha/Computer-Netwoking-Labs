def check_even_parity(binary_pattern_with_parity):
    # Check if the input is a valid binary string
    if not all(bit in '01' for bit in binary_pattern_with_parity):
        raise ValueError("Input should be a binary string")

    # Count the number of 1s in the binary pattern including the parity bit
    count_of_ones = binary_pattern_with_parity.count('1')
    
    # Check if the count of 1s is even (valid parity)
    if count_of_ones % 2 == 0:
        return True  # Parity is valid
    else:
        return False  # Parity is invalid

# Get binary pattern with parity from user input
binary_pattern_with_parity = input("Enter a binary pattern with parity bit: ")
try:
    is_valid_parity = check_even_parity(binary_pattern_with_parity)
    print(f"Pattern with parity: {binary_pattern_with_parity}")
    print(f"Is the parity valid? {'Yes' if is_valid_parity else 'No'}")
except ValueError as e:
    print(e)
