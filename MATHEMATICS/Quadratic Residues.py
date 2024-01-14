# Given prime modulus
p = 29

# List of integers to find quadratic residues for
ints = [14, 6, 11]

# Function to find the quadratic residue and its smaller root
def quadratic_residue(x, p):
    # Iterate through possible values of 'a'
    for a in range(1, p):
        # Check if a^2 is congruent to x modulo p
        if (a**2) % p == x:
            # Return the smaller root
            return p - a

    return None

# Iterate through the list of integers
for x in ints:
    # Find the quadratic residue and its smaller root
    result = quadratic_residue(x, p)
    
    # Display the result
    if result:
        smaller_root = result
        print(smaller_root)
    else:
        print("No quadratic residue found")
