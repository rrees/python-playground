
def a_string(s):
	chrs = list(s)
	c = s[0]
	i = 0
	j = len(chrs) - 1

	while i < j:
		c = chrs[i]
		chrs[i] = chrs[j]
		chrs[j] = c
		j = j - 1
		i = i + 1

	return "".join(chrs)
