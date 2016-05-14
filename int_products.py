import functools

def calculate(ints):


	left = 1
	rights = [1]

	for i in range(len(ints) - 1, 0, -1):
		rights = [ints[i] * rights[0]] + rights

	totals = []
	for i in ints:
		totals.append(left * rights[0])

		left = left * i
		rights = rights[1:]

	return totals

def calculate_brute_force(ints):

	result = []

	for i in range(0, len(ints)):
		total = None

		for j in range(0, len(ints)):
			if i == j:
				continue

			if total == None:
				total = ints[j]
			else:
				total = total * ints[j]

		result.append(total)


	return result


def calculate_lists(ints):

	def product(ints):
		return functools.reduce(lambda acc, val: acc * val, ints)

	if len(ints) < 2:
		return ints

	results = []

	for idx, i in enumerate(ints):
		if idx == 0:
			results.append(product(ints[1:]))
		elif idx == len(ints) - 1:
			results.append(product(ints[0:-1]))
		else:
			results.append(product(ints[0:idx] + ints[idx+1:]))
	return results
