# A tea stall offers different prices for different cup sizes.
# Write a program that calculates the price based on size.

# Task:
#  - Input:"small","medium","large"
#  - Small -> Rs 10, Medium -> rs 15, Large -> rs 20
#  - If invalid: show "Unknown cup size"

cup = input("Choice your cup size (small/medium/large): ").lower()

if cup == "small":
    print("Price is 10 rupees")
elif cup == "medium":
    print("Price is 15 rupees")
elif cup == "large":
    print("Price is 20 rupees")
else:
    print("Unknown cup size")

# Choice your cup size (small/medium/large): small
# Price is 10 rupees

# Choice your cup size (small/medium/large): extra large
# Unknown cup size