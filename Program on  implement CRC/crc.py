def xor(a, b):
    # Perform XOR operation on two binary strings
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2div(dividend, divisor):
    # Perform Modulo-2 division
    pick = len(divisor)
    tmp = dividend[:pick]
    
    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0'*pick, tmp) + dividend[pick]
        pick += 1
    
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)
    
    return tmp

def encode_data(data, key):
    l_key = len(key)
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder
    return codeword

def decode_data(data, key):
    remainder = mod2div(data, key)
    return remainder

# Example usage
data = "11010011101100"
key = "1011"

print("Original data: ", data)
encoded_data = encode_data(data, key)
print("Encoded data with CRC: ", encoded_data)

remainder = decode_data(encoded_data, key)
print("Remainder after decoding: ", remainder)
print("Is data valid?: ", all(c == '0' for c in remainder))
