import copy

def swap(i, j, array):
	item = array[i]
	array[i] = array[j]
	array[j] = item
	return array

def permutations(array, n = None, results = None):

	if not n:
		n = len(array)

	if not results:
		results = []

	if n == 1:
		results.append(copy.deepcopy(array))
		return results

	for i in range(n - 1):
		results = permutations(array, n - 1, results)
		if n % 2 == 0:
			swap(i, n - 1, array)
		else:
			swap(0, n - 1, array)

	results = permutations(array, n - 1, results)

	return results
