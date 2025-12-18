# You want to simulate tea heating.
# It start at 40c and boils at 100c.
# Task:
#  - Use a while loop.
#  - Increase temperature by 15 until it reaches or exceeds 100.
#  - Print each temperature step.

temperature = 40

while temperature < 100:
    print(f"Current temperature: {temperature}")
    # temperature = temperature + 15
    temperature +=15

print("Tea is ready to boil")     