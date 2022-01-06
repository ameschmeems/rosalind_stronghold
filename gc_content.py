def gc_content(file_path: str):

	max_gc = 0

	with open(file_path) as f:
		content = f.readlines()
		for i, line in enumerate(content):
			if line.startswith('>'):
				id = line[1:]
				seq = ""
			else:
				newseq = line.strip()
				seq = seq + newseq
				if i == len(content) - 1 or content[i + 1].startswith('>'):
					gc = 100 * (seq.count('C') + seq.count('G')) / len(seq)
					if gc > max_gc:
						max_gc = gc
						max_id = id
	print(max_id, end = '')
	print(max_gc)