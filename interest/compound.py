import sys

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

print(
    f"Principle: {principle}; base daily interest {daily_interest:.2f}, adjusted daily interest {adjusted_daily_interest:.2f}"
)

i = 10
current_balance = principle

while i > 0:
    daily_interest = calculate_daily_interest(current_balance, interest_rate)
    print(f"Balance: {current_balance:.2f}, daily interest {daily_interest:.2f}")
    current_balance = current_balance + daily_interest
    i = i - 1

print()

i = 10
current_balance = principle + adjustment

while i > 0:
    daily_interest = calculate_daily_interest(current_balance, interest_rate)
    print(f"Balance: {current_balance:.2f}, daily interest {daily_interest:.2f}")
    current_balance = current_balance + daily_interest
    i = i - 1
