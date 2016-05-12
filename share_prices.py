
def calculate_margin(prices):

	min = None
	max = None
	best_margin = None

	for price in prices:
		if not min:
			min = price
			continue

		if price < min:
			min = price

		if not max:
			max = price
			continue

		if price > max:
			max = price

		margin = max - min

		if not best_margin or margin > best_margin:
			best_margin = margin
			min = None
			max = None

	return best_margin
