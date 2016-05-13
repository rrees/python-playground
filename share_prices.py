
def calculate_margin(prices):
	best_margin = None
	
	for idx, price in enumerate(prices):
		for next_price in prices[1 + idx:]:
			margin = next_price - price

			if not best_margin:
				best_margin = margin
			else:
				if margin > best_margin:
					best_margin = margin

	return best_margin
