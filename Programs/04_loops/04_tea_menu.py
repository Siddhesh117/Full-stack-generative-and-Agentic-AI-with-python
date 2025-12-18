# You're creating a tea menu board.
# Each item must be numbered.
# Task:
#  - Use enumerate() to print menu items with numbers.


menu = ["Green", "Lemon", "Spiced", "Mint"]

# for m in menu:
#     print(f"Menu item is {m}")
    
for idx, item in enumerate(menu, start=1):
    print(f"{idx} : {item} chai")

# 1 : Green chai
# 2 : Lemon chai
# 3 : Spiced chai
# 4 : Mint chai    