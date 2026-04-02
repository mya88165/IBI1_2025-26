# defining input and output files 
input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = "stop_genes.fa"

# define stop codons 
stop_codons = ["TAA", "TAG", "TGA"]

def get_gene_name(header):
    parts = header.split()         # split header into words 
    first_part = parts[0]          # something like >YBR024W_mRNA
    gene_name = first_part[1:]     # remove >
    return gene_name

def find_in_frame_stop_codons(seq):
    found_stops = set()

    for i in range(0, len(seq) - 2, 3):     # searches in codons instead of looking for codons in every position 
        if seq[i:i+3] == "ATG":
            for j in range(i, len(seq) - 2, 3):
                codon = seq[j:j+3]
                if codon in stop_codons:
                    found_stops.add(codon)
                    break

    return sorted(found_stops)


with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    header = ""             # store current header 
    sequence_parts = []     # store sequnce lines 

    # read file line by line 
    for line in infile:
        line = line.strip()

        if line.startswith(">"):    # if line is a header 
            if header != "":
                sequence = "".join(sequence_parts)      # combine sequence 
                gene_name = get_gene_name(header)
                stops = find_in_frame_stop_codons(sequence)

                if stops:
                    outfile.write(f">{gene_name} {' '.join(stops)}\n")
                    outfile.write(sequence + "\n")
        
             # store new header and reset sequence 
            header = line
            sequence_parts = []
        else:
            sequence_parts.append(line)

    # process the last sequence
    if header != "":
        sequence = "".join(sequence_parts)
        gene_name = get_gene_name(header)
        stops = find_in_frame_stop_codons(sequence)

        if stops:
            outfile.write(f">{gene_name} {' '.join(stops)}\n")
            outfile.write(sequence + "\n")

print("Done. Output written to stop_genes.fa")