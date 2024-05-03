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


def display_projection(principle, interest_rate, adjustment, days=30):
    base_projection = interest_projection(principle, interest_rate)
    adjusted_projection = interest_projection(principle + adjustment, interest_rate)

    for [[base_balance, base_interest], [adjusted_balance, adjusted_interest]] in zip(
        islice(base_projection, days), islice(adjusted_projection, days)
    ):
        balance_difference = adjusted_balance - base_balance - adjustment
        interest_difference = adjusted_interest - base_interest
        print(
            f"Balance: {adjusted_balance:.2f} ({balance_difference:.2f}), daily interest {adjusted_interest:.2f} ({interest_difference:.2f})"
        )


display_projection(principle, interest_rate, adjustment)
