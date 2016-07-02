
def subsets(a_set, subset_size, depth = 0, all_subsets = None, current_sub_set=None):
	print(a_set, subset_size, depth, all_subsets, current_sub_set)
	if current_sub_set == None:
		current_sub_set = []

	if all_subsets == None:
		a_set = sorted(a_set)
		all_subsets = []

	if len(current_sub_set) == subset_size:
		all_subsets.append(current_sub_set)
		return

	assert depth <= subset_size, "Recursion exceeded the sought-for length"

	def next_set(a_set, idx):
		if idx == 0:
			return a_set[1:]

		if not a_set:
			return []

		return a_set[0:idx] + a_set[idx+1: len(a_set)]

	for i in range(len(a_set)):
		subsets(next_set(a_set,i), subset_size, depth = depth + 1, all_subsets = all_subsets, current_sub_set = current_sub_set.copy() + a_set[i:i+1])

	return all_subsets