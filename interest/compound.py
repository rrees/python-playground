import sys

from itertools import islice

principle = float(sys.argv[1])

interest_rate = float(sys.argv[2])

adjustment = float(sys.argv[3])


def calculate_daily_interest(principle, interest_rate):
    total_interest = (principle * interest_rate) / 100

    return total_interest / 365


daily_interest, adjusted_daily_interest = (
    calculate_daily_interest(principle, interest_rate),
    calculate_daily_interest(principle + adjustment, interest_rate),
)


def interest_projection(principle, rate):
    total = principle
    while True:
        daily_interest = calculate_daily_interest(total, rate)
        total = total + daily_interest
        yield (total, daily_interest)


print(
    f"Principle: {principle}; base daily interest {daily_interest:.2f}, adjusted daily interest {adjusted_daily_interest:.2f}"
)

base_projection = interest_projection(principle, interest_rate)
adjusted_projection = interest_projection(principle + adjustment, interest_rate)

days = 10

for current_balance, daily_interest in islice(base_projection, 10):
    print(f"Balance: {current_balance:.2f}, daily interest {daily_interest:.2f}")

print()

for current_balance, daily_interest in islice(adjusted_projection, 10):
    print(f"Balance: {current_balance:.2f}, daily interest {daily_interest:.2f}")
