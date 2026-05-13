def read_fasta(filename):
    name = ""
    sequence = ""

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith(">"):
                name = line[1:]
            else:
                sequence += line

    return name, sequence

def percentage_identity(seq1, seq2):
    identical = 0

    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            identical += 1

    percentage = (identical / len(seq1)) * 100
    return percentage

def hamming_distance(seq1, seq2):
    distance = 0

    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            distance += 1

    return distance

def blosum_score(seq1, seq2, blosum62):
    total_score = 0

    for i in range(len(seq1)):
        aa1 = seq1[i]
        aa2 = seq2[i]

        score = blosum62[aa1][aa2]
        total_score += score

    normalised_score = total_score / len(seq1)

    return total_score, normalised_score

def compare_sequences(file1, file2, blosum62):
    name1, seq1 = read_fasta(file1)
    name2, seq2 = read_fasta(file2)

    if len(seq1) != len(seq2):
        print("Error: sequences are not the same length.")
        return

    identity = percentage_identity(seq1, seq2)
    distance = hamming_distance(seq1, seq2)
    raw_score, normalised_score = blosum_score(seq1, seq2, blosum62)

    print("Comparison:", name1, "vs", name2)
    print("Length:", len(seq1), "amino acids")
    print("Percentage identity:", round(identity, 2), "%")
    print("Hamming distance:", distance)
    print("BLOSUM62 raw score:", raw_score)
    print("BLOSUM62 normalised score:", round(normalised_score, 2))
    print()


blosum62 = {}

amino_acids = "ARNDCQEGHILKMFPSTWYV"

for aa1 in amino_acids:
    blosum62[aa1] = {}

    for aa2 in amino_acids:
        if aa1 == aa2:
            blosum62[aa1][aa2] = 4
        else:
            blosum62[aa1][aa2] = -1


compare_sequences("human_dlx5.fasta", "mouse_dlx5.fasta", blosum62)
compare_sequences("human_dlx5.fasta", "random.fasta", blosum62)
compare_sequences("mouse_dlx5.fasta", "random.fasta", blosum62)