# Federal Income Tax Calculator (2009 rates)

# Define tax brackets as a dictionary keyed by filing status
brackets = {
    0: [  # Single
        (8350, 0.10),
        (33950, 0.15),
        (82250, 0.25),
        (171550, 0.28),
        (372950, 0.33),
        (float("inf"), 0.35)
    ],
    1: [  # Married Filing Jointly or Qualified Widow(er)
        (16700, 0.10),
        (67900, 0.15),
        (137050, 0.25),
        (208850, 0.28),
        (372950, 0.33),
        (float("inf"), 0.35)
    ],
    2: [  # Married Filing Separately
        (8350, 0.10),
        (33950, 0.15),
        (68525, 0.25),
        (104425, 0.28),
        (186475, 0.33),
        (float("inf"), 0.35)
    ],
    3: [  # Head of Household
        (11950, 0.10),
        (45500, 0.15),
        (117450, 0.25),
        (190200, 0.28),
        (372950, 0.33),
        (float("inf"), 0.35)
    ]
}


def compute_tax(status, income):
    tax = 0.0
    prev_limit = 0

    for limit, rate in brackets[status]:
        if income > limit:
            tax += (limit - prev_limit) * rate
            prev_limit = limit
        else:
            tax += (income - prev_limit) * rate
            break

    return tax


def main():
    print("Choose filing status:")
    print("0 - Single")
    print("1 - Married Filing Jointly or Qualified Widow(er)")
    print("2 - Married Filing Separately")
    print("3 - Head of Household")

    status = int(input("Status: "))
    income = float(input("Enter taxable income: "))

    tax = compute_tax(status, income)
    print(f"Your total tax is: ${tax:.2f}")


if __name__ == "__main__":
    main()
