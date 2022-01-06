def consensus_and_profile(file_path: str):

	sequences = []

	with open(file_path) as f:
		content = f.readlines()
		for i, line in enumerate(content):
			if line.startswith('>'):
				seq = ""
			else:
				newseq = line.strip()
				seq += newseq
				if i == len(content) - 1 or content[i+1].startswith('>'):
					sequences.append(seq)
	n = len(sequences[0])
	profile_matrix = {
		"A": [0]*n,
		"C": [0]*n,
		"G": [0]*n,
		"T": [0]*n
	}

	for dna in sequences:
		for position, nucleotide in enumerate(dna):
			profile_matrix[nucleotide][position] += 1
	
	consensus_string = ""
	for position in range(n):
		max_count = 0
		max_nucleotide = None
		for nucleotide in ["A", "C", "G", "T"]:
			count = profile_matrix[nucleotide][position]
			if count > max_count:
				max_count = count
				max_nucleotide = nucleotide
		consensus_string += max_nucleotide
	
	with open("file.txt", "w") as file:
		print(f"{consensus_string}", file = file, end = '')
		for key in profile_matrix:
			print(f"\n{key}: ",file = file, end = '')
			for i in range(len(profile_matrix[key])):
				print(f"{profile_matrix[key][i]} ", file = file, end = '')
