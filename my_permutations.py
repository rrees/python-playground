
def subsets(a_set, subset_size, depth = 0, all_subsets = None, current_sub_set=None):
	assert subset_size <= len(a_set), "Cannot create subsets larger than the input set"
	
	if current_sub_set == None:
		current_sub_set = []

	if all_subsets == None:
		all_subsets = []

	if len(current_sub_set) == subset_size:
		all_subsets.append(current_sub_set)
		return

	assert depth <= subset_size, "Recursion exceeded the sought-for length"

	for i in a_set:
		if i in current_sub_set:
			continue
		subsets(a_set, subset_size, depth = depth + 1, all_subsets = all_subsets, current_sub_set = current_sub_set.copy() + [i])

	return all_subsets