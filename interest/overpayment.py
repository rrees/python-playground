import sys

from itertools import islice

if len(sys.argv) != 4:
    print("python compound.py <principle> <rate> <amount added or removed (-)>")
    exit(1)


principle = float(sys.argv[1])

interest_rate = float(sys.argv[2])

adjustment = float(sys.argv[3])


def calculate_interest(principle, interest_rate):
    monthly_interest_rate = interest_rate / 12

    monthly_interest = (principle * monthly_interest_rate) / 100

    daily_interest = monthly_interest / 30

    return monthly_interest, daily_interest


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

    for [
        day,
        [[base_balance, base_interest], [adjusted_balance, adjusted_interest]],
    ] in enumerate(
        zip(islice(base_projection, days), islice(adjusted_projection, days))
    ):
        balance_difference = adjusted_balance - base_balance - adjustment

        print(
            f"Day {day + 1}: balance: {adjusted_balance:.2f} ({balance_difference:.2f}); daily interest {calculate_daily_interest(adjusted_balance, interest_rate):.2f}"
        )


[initial_monthly_interest, initial_daily_interest] = calculate_interest(
    principle, interest_rate
)
print(
    f"Monthly interest: {initial_monthly_interest:.2f}; daily interest {initial_daily_interest:.2f}"
)

[adjusted_monthly_interest, adjusted_daily_interest] = calculate_interest(
    principle + adjustment, interest_rate
)

print("After adjustment:")
print(
    f"Monthly interest: {adjusted_monthly_interest:.2f}; daily interest {adjusted_daily_interest:.2f}"
)
print()

display_projection(principle, interest_rate, adjustment)
