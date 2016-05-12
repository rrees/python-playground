
def calculate_margin(prices):

	min = None
	max = None
	best_margin = None

	for price in prices:
		if not min:
			min = price
			continue

		if not max:
			if price > min:
				max = price
				continue

		if price < min:
			min = price

		if price > max:
			max = price

		best_margin = max - min

	return best_margin
