# A local cafe wants a program that suggested a snack.
# If Customer asks for cookies or samosa, it confirms the order.ordOtherwise, it says it's not available.set

# Task:
#  - Take snack input
#  - If it's "cookies" or "samosa", confirm the order
#  - Else, show unavailability    

snack = input("Enter your preferred snack: ").lower()

if snack == "cookies" or snack == "samosa":
    print(f"Great Choice! We'll serve you {snack}")
else:
    print("Sorry, we only serve cookies or samosa with tea")    

# Enter your preferred snack: samosa
# Great Choice! We'll serve you samosa

# Enter your preferred snack: Chai
# Sorry, we only serve cookies or samosa with tea