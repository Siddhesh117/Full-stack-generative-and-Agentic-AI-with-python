
#   Note :  Walrus Operator :=

# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is {remainder}")

# # Not divisible, remainder is 3    

# value = 13

# if (remainder := value % 5):
#     print(f"Not divisible, remainder is {remainder}")

# # Not divisible, remainder is 3    

# value = 13

# if (remainder := value % 5):
#     print(f"Not divisible, remainder is {remainder}")


# available_sizes = ["small", "medium", "large"] 

# if((requested_size := input("Enter your chai size: "))) in available_sizes:
#     print(f"Serving {requested_size} chai")
# else:
#     print(f"Size is unavailable - {requested_size}")    


# Enter your chai size: small
# Serving small chai

# Enter your chai size: min
# Size is unavailable - min

flavours = ["masala","ginger","lemon","mint"]

print("Available flavors: ",flavours)

while (flavour := input("Choose your flavor: ")) not in flavours:
    print(f"Sorry, {flavour} is not available")
print(f"You choose {flavour} chai")    


# Available flavors:  ['masala', 'ginger', 'lemon', 'mint']
# Choose your flavor: lemon
# You choose lemon chai

# Available flavors:  ['masala', 'ginger', 'lemon', 'mint']
# Choose your flavor: tea
# Sorry, tea is not available
# Choose your flavor: 