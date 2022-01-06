def point_mutations(file_path: str) -> int:

	count = 0

	with open(file_path) as f:
		content = f.readlines()
		s = content[0]
		t = content[1]
		for i in range(len(s)):
			if s[i] != t[i]:
				count += 1
	return count