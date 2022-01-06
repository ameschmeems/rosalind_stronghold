def motif(s: str, t: str) -> list:

	lst = []

	for i in range(len(s)):
		for j in range(len(t)):
			if not (s[i+j] == t[j]):
				break
			if j == (len(t) - 2):
				lst.append(i + 1)
	return lst

if __name__ == "__main__":
	
	with open("/home/kpucylo/Downloads/rosalind_subs.txt") as f:
		lines = f.readlines()
		s = lines[0]
		t = lines[1]
	
	lst = motif(s, t)
	
	for i in range(len(lst)):
		print(lst[i])
