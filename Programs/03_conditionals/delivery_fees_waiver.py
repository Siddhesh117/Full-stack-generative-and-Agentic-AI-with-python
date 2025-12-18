# You run an online tea store.
# If the order amount is more than Rs 300, delivery is free;
# otherwise, it costs Rs 30.

# Task:
#  - Input: order_amount
#  - Use ternary operator to decide delivery fee

# convert number
order_amount = int(input("Enter the order amount: "))

# print(f"Order amount: {type(order_amount)}")

#  ternary operator
delivery_fees = 0 if order_amount > 300 else 30

print(f"Delivery fees is: {delivery_fees}")
