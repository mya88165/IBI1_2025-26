seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

# define start and stop codons 
start_codon = "AUG"
stop_codons = ["UAA", "UAG", "UGA"]

largest_orf = ""

# loop through every position in the sequence 
for i in range(len(seq) - 2):
    codon = seq[i:i+3] # to see the full codon 

    if codon == start_codon:
        for j in range(i, len(seq) - 2, 3): # move forward in steps of three 
            current_codon = seq[j:j+3]

            if current_codon in stop_codons:
                orf = seq[i:j+3]
                if len(orf) > len(largest_orf):
                    largest_orf = orf
                break

print("Largest ORF:", largest_orf)
print("Length:", len(largest_orf))