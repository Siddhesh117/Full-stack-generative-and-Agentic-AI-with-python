# Some chai flavors are out of stock.
# You want to skip those and stop entirely if
# someone requests a restricted flavor.
# Task:
#  - Skip is flavor is "Out of Stock"
#  - Break if flavor is "Discontinued"



flavours = ["Ginger","Out of Stock", "Lemon","Discontinued","Tulsi"]

for flavour in flavours:
    if flavour == "Out of Stock":
        continue
    if flavour == "Discontinued":
        print(f"{flavour} item found")  
        break
    print(f"{flavour} item found")  
    # print("Discontinued item found")  

print(f"Out side of loop")    


# Ginger item found
# Lemon item found
# Discontinued item found
# Out side of loop



#  if flavour == "Discontinued":
#         break
#  print(f"{flavour} item found")  
# Ginger item found
# Lemon item found
# Out side of loop


# if flavour == "Discontinued":
#         print(f"{flavour} item found")  
#         break
# Discontinued item found
# Out side of loop