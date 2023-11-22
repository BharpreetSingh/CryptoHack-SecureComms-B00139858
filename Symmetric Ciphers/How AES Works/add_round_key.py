state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    return bytes(sum(matrix, []))

def add_round_key(s, k):
    # Goes through each element of the state matrix and XOR it with the corresponding element of the round key matrix
    for x in range(4):
        for y in range(4):
            s[x][y] = s[x][y] ^ k[x][y]

    return s

# Call the add_round_key function and then use matrix2bytes to convert the result to a 16-byte array
result_matrix = add_round_key(state, round_key)
result_bytes = matrix2bytes(result_matrix)

# Print the result
print(result_bytes)

