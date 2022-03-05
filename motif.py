def motif(s: str, t: str) -> list:

	lst = []

	for i in range(len(s)):
		for j in range(len(t)):
			if not (s[i+j] == t[j]):
				break
			if j == (len(t) - 2):
				lst.append(i + 1)
	return lst
