# Create a function called protein_mass
# It will calculate the total mass of an amino acid sequence
def protein_mass(sequence):
    # Create a dictionary containing amino acids and their masses
    # Key = amino acid letter
    # Value = mass in amu
    amino_acid_masses = {
        "G": 57.02,
        "A": 71.04,
        "S": 87.03,
        "P": 97.05,
        "V": 99.07,
        "T": 101.05,
        "C": 103.01,
        "I": 113.08,
        "L": 113.08,
        "N": 114.04,
        "D": 115.03,
        "Q": 128.06,
        "K": 128.09,
        "E": 129.04,
        "M": 131.04,
        "H": 137.06,
        "F": 147.07,
        "R": 156.10,
        "Y": 163.06,
        "W": 186.08
    }

    # Start total mass at zero
    total_mass = 0

    # Go through each amino acid in the sequence one by one
    for amino_acid in sequence:

        # Check if the amino acid exists in the dictionary
        if amino_acid in amino_acid_masses:

            # Add its mass to the running total
            total_mass += amino_acid_masses[amino_acid]

        else:
            # If amino acid is invalid, stop and show error message
            return f"Error: '{amino_acid}' has no recorded mass."

    # After loop finishes, return total mass
    return total_mass


# Example valid sequence
example_sequence = "ACDE"

# Call function and print result
print("Protein mass:", protein_mass(example_sequence))

# Test invalid sequence containing letters not in dictionary
print(protein_mass("ACZX"))