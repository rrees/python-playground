import functools

def calculate(ints):

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
