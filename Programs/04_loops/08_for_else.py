staff = [("Amit", 16), ("Zara", 17), ("Raj", 15)]

# for name, age in staff:
#     if age >= 18:
#         print(f"{name} is eligible to manage the staff")
#         break
#     else:
#         print(f"No one is eligible to manage the staff")    


# No one is eligible to manage the staff
# No one is eligible to manage the staff
# No one is eligible to manage the staff


# foll back statement else part not in if block 
for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible to manage the staff")
        break
else:
    print(f"No one is eligible to manage the staff")

# No one is eligible to manage the staff    


for name, age in staff:
    if age <= 18:
        print(f"{name} is eligible to manage the staff")
        break
    else:
        print(f"No one is eligible to manage the staff") 

# Amit is eligible to manage the staff

for name in staff:
    if age <= 18:
        print(f"{name} is eligible to manage the staff")
        break
    else:
        print(f"No one is eligible to manage the staff") 

# ('Amit', 16) is eligible to manage the staff        