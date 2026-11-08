expenses = [350, 200, 100, 15, 50]
total = 0
plus_100 = 0

if len(expenses) != 0:
    for number in expenses:
        total += number
        if number > 100:
            plus_100 += 1

    max_num = max(expenses)
    min_num = min(expenses)
    average_cost = total / len(expenses)
    print("===== EXPENSE SUMMARY =====")
    print("  Total expenses:", total, "EUR")
    print("  Average expense:", average_cost, "EUR")
    print("  Highest expense:", max_num, "EUR")
    print("  Lowest expense:", min_num, "EUR")
    print("  Expenses over 100 EUR:", plus_100)
    print("===========================")
else:
    print("No available data")


