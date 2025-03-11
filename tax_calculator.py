# -*- coding: utf-8 -*-  # UTF-8 인코딩 설정 (이모지 & 한글 지원)

def calculate_tax(income):
    """
    Calculate estimated federal income tax based on 2024 US tax brackets.
    """
    TAX_BRACKETS = [
        (11000, 0.10),  # Up to $11,000 -> 10%
        (44725, 0.12),  # $11,001 ~ $44,725 -> 12%
        (95375, 0.22),  # $44,726 ~ $95,375 -> 22%
        (182100, 0.24), # $95,376 ~ $182,100 -> 24%
        (231250, 0.32), # $182,101 ~ $231,250 -> 32%
        (578125, 0.35), # $231,251 ~ $578,125 -> 35%
        (float('inf'), 0.37)  # Above that -> 37%
    ]

    tax = 0
    previous_bracket = 0

    for bracket, rate in TAX_BRACKETS:
        if income > bracket:
            tax += (bracket - previous_bracket) * rate
            previous_bracket = bracket
        else:
            tax += (income - previous_bracket) * rate
            break

    return tax

# Get user input
income = float(input("Enter your annual income ($): "))

# Calculate tax
tax_amount = calculate_tax(income)
after_tax_income = income - tax_amount

# Print results
print("\n📌 Estimated Tax: ${:,.2f}".format(tax_amount))
print("💰 After-Tax Income: ${:,.2f}".format(after_tax_income))

