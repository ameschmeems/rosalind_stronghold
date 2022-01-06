def rna_to_protein(file_path: str) -> str:

	codon_table = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "UCU": "S",
					"UCC": "S", "UCA": "S", "UCG": "S", "UAU": "Y", "UAC": "Y",
					"UAA": "STOP", "UAG": "STOP", "UGU": "C", "UGC": "C", "UGA": "STOP",
					"UGG": "W", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
					"CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P", "CAU": "H",
					"CAC": "H", }