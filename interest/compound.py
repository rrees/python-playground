import sys

principle = float(sys.argv[1])

interest_rate = float(sys.argv[2])

days = int(sys.argv[3])

running_total = principle
for _ in range(days):
    total_interest = running_total * (interest_rate / 100)
    running_total += total_interest / 365
    # print(running_total)

print(f"Total after {days} days: {running_total:.2f}")
