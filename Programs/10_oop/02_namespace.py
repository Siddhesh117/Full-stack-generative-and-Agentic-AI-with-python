class Chai:
    origin = "India"

print(Chai.origin)    
# India

Chai.is_hot = True
print(Chai.is_hot)
# True

# creating objects from class Chai

masala = Chai()
print(f"Masala {masala.origin}") # Masala India
print(f"Masala {masala.is_hot}") # Masala True

masala.is_hot = False
print(f"Masala {masala.is_hot}") # Masala False
print(f"Masala {Chai.is_hot}") # Masala True