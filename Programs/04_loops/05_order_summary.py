# You're preparing an order summary with customer names
# and their total bill.
# Task:
#  - Use two lists: one of names and one of bills.
#  - Print: "[Name] paid Rs[amount]"

names = ["Hitesh", "Meera", "Sam", "Ali"]
bills = [50, 70, 100, 55]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")

# Hitesh paid 50 rupees
# Meera paid 70 rupees
# Sam paid 100 rupees
# Ali paid 55 rupees
