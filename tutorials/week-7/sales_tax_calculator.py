def calculate_tax(cost_total: float):
    tax_rate = 0.06

    tax_owed = round(float(tax_rate * cost_total), 2)
    print(f"Sales tax:\t\t\t\t{tax_owed}")

    total_after_tax = cost_total + tax_owed
    print(f"Total after tax:\t\t\t{total_after_tax}")
