
def swap(i, j, array):
	item = array[i]
	array[i] = array[j]
	array[j] = item
	return array

def permutations(array, n = None, results = None):
	print(array, n, results)

	if not n:
		n = len(array)

	if not results:
		results = []

	if n == 1:
		print(array, results)
		results.append(array.copy())
		print(array, results)
		return results

	for i in range(n):
		results = permutations(array, n - 1, results)
		if n % 2 == 0:
			swap(i, -1, array)
		else:
			swap(0, -1, array)

	return results