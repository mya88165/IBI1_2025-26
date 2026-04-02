import matplotlib.pyplot as plt

input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
valid_stops = ["TAA", "TAG", "TGA"]


def read_fasta(filename):
    sequences = []
    header = ""
    sequence_parts = []

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith(">"):
                if header != "":
                    sequences.append((header, "".join(sequence_parts)))
                header = line          # store new header 
                sequence_parts = []    # reset sequence list for new genes 
            else:
                sequence_parts.append(line)

        if header != "":
            sequences.append((header, "".join(sequence_parts)))

    return sequences


def longest_orf_with_stop(seq, chosen_stop):     # find longer ORF ending with chosen stop codon 
    longest_orf = ""

    for i in range(len(seq) - 2):
        if seq[i:i+3] == "ATG":
            for j in range(i, len(seq) - 2, 3):
                codon = seq[j:j+3]
                if codon in valid_stops:
                    if codon == chosen_stop:
                        orf = seq[i:j+3]
                        if len(orf) > len(longest_orf):
                            longest_orf = orf
                    break

    return longest_orf


def count_codons_in_orf(orf, codon_counts):     # count codons in ORF tag
    for i in range(0, len(orf) - 2, 3):
        codon = orf[i:i+3]
        codon_counts[codon] = codon_counts.get(codon, 0) + 1


chosen_stop = input("Enter a stop codon (TAA, TAG, TGA): ").upper()

if chosen_stop not in valid_stops:      # check if input is valid 
    print("Invalid stop codon")
    exit()

sequences = read_fasta(input_file)
codon_counts = {}

for header, seq in sequences:       # loop through sequence 
    orf = longest_orf_with_stop(seq, chosen_stop)      # find longest ORF for this gene 
    if orf != "":
        count_codons_in_orf(orf, codon_counts)

print("Codon counts:")
for codon, count in sorted(codon_counts.items()):
    print(codon, count)     # print codon and its frequency 

labels = list(codon_counts.keys())      
sizes = list(codon_counts.values())

plt.figure(figsize=(10, 10))
plt.pie(sizes, labels=labels)
plt.title(f"Codon distribution for genes containing stop codon {chosen_stop}")
plt.savefig(f"{chosen_stop}_codon_pie_chart.png")
print(f"Pie chart saved as {chosen_stop}_codon_pie_chart.png")
