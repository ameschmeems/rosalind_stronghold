def rna_to_protein(file_path: str) -> str:

	codon_table = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "UCU": "S",
					"UCC": "S", "UCA": "S", "UCG": "S", "UAU": "Y", "UAC": "Y",
					"UAA": "STOP", "UAG": "STOP", "UGU": "C", "UGC": "C", "UGA": "STOP",
					"UGG": "W", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
					"CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P", "CAU": "H",
					"CAC": "H", "CAA": "Q", "CAG": "Q", "CGU": "R", "CGC": "R",
					"CGA": "R", "CGG": "R", "AUU": "I", "AUC": "I", "AUA": "I",
					"AUG": "M", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
					"AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGU": "S",
					"AGC": "S", "AGA": "R", "AGG": "R", "GUU": "V", "GUC": "V",
					"GUA": "V", "GUG": "V", "GCU": "A", "GCC": "A", "GCA": "A",
					"GCG": "A", "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
					"GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}
	protein = ""

	with open(file_path) as f:
		rna = f.read()
	
	for i in range(0, len(rna), 3):
		current_codon = rna[i:i+3]
		if codon_table[current_codon] == "STOP":
			break
		protein += codon_table[current_codon]
	return protein

if __name__ == "__main__":
	print(rna_to_protein("/home/kpucylo/Downloads/rosalind_prot.txt"))
		