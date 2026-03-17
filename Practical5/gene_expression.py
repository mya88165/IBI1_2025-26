import matplotlib.pyplot as plt

# key = gene name 
# value = expression value 

gene_expression = {
    "TP53": 12.4,
    "EGFR": 15.1,
    "BRCA1": 8.2,
    "PTEN": 5.3,
    "ESR1": 10.7
}

print("Initial gene expression dictionary:")
print(gene_expression)

gene_expression["MYC"] = 11.6

# added MYC 
print("\nUpdated gene expression dictionary:")
print(gene_expression)

genes = list(gene_expression.keys())
values = list(gene_expression.values())

plt.figure()
plt.bar(genes, values)
plt.xlabel("Gene")
plt.ylabel("Expression Level")
plt.title("Gene Expression Levels")
plt.show()

# expression value of a	selected gene
gene_of_interest = "TP53"

if gene_of_interest in gene_expression:
    print(f"\nExpression value for {gene_of_interest}: {gene_expression[gene_of_interest]}")
else:
    print(f"\nError: {gene_of_interest} is not present in the dataset.")

average_expression = sum(gene_expression.values()) / len(gene_expression)
print(f"\nAverage gene expression level: {average_expression:.2f}")