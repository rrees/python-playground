
def of_two(n, sum=0, current_power=1):

	if n == 0:
		return sum

	sum = sum + current_power

	return of_two(n - 1, sum, current_power << 1)

